import sys
import boto3
import json
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# --- Fetch Snowflake creds from Secrets Manager ---
secret_name = "glue-snowflake-up"
region_name = "us-east-1"

session = boto3.session.Session()
client = session.client(service_name="secretsmanager", region_name=region_name)

get_secret_value_response = client.get_secret_value(SecretId=secret_name)
secret_dict = json.loads(get_secret_value_response["SecretString"])

# --- Map Snowflake options ---
sfOptions = {
    "sfURL": "RBMZUUC-MXC36607.snowflakecomputing.com",    # 🔹 hardcode
    "sfDatabase": "O2BKIDS_DB",                  # 🔹 hardcode
    "sfSchema": "GLUE",                          # 🔹 hardcode
    "sfWarehouse": "DEV_WAREHOUSE",                 # 🔹 hardcode
    "sfRole": "GLUE_ROLE",                    # optional, if required
    "sfUser": secret_dict["username"],           # from secret
    "sfPassword": secret_dict["password"]        # from secret
}

# --- Example DataFrame ---
data = [("bhagi", 5), ("latha", 70), ("shiva", 385)]
columns = ["NAME", "AGE"]
df_write = spark.createDataFrame(data, columns)

# --- Write to Snowflake ---
(
    df_write.write
    .format("snowflake")
    .options(**sfOptions)
    .option("dbtable", "USERS")   # ✅ only table name, since db & schema already given
    .mode("append")
    .save()
)
