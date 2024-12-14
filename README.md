# React Application Deployment Using AWS S3 and CloudFront

This project explains the **developer workflow** and **user workflow** for deploying a React application using AWS services like S3, CloudFront, IAM, and Lambda.

---

## Developer Workflow

![aws_project drawio (2)](https://github.com/user-attachments/assets/6807b191-b328-48cb-b58f-b751bca94894)

The following steps describe the **developer process** for deploying the application:

1. **Code Push**  
   Developers write and push their code to the GitHub repository.

2. **GitHub Actions**  
   - GitHub Actions automatically trigger the deployment process.  
   - The React code is built and deployed to an **S3 bucket**.

3. **CloudFront Integration**  
   - Content from the S3 bucket is served via **CloudFront** (a Content Delivery Network).  
   - This ensures fast and secure delivery of the application.

4. **Cache Clearing with Lambda**  
   - When new images or content are uploaded to the S3 bucket, an AWS **Lambda function** clears the CloudFront cache.  
   - This ensures the updated content is displayed to users immediately.

---

## User Workflow

![usrworkflow](https://github.com/user-attachments/assets/48c98bd2-cf4f-4f4b-972a-2a01db43ea16)

The following steps describe how **end users** access the application:

1. **Accessing the Application**  
   Users visit the website through a custom domain (managed via **Route53**).

2. **Content Delivery**  
   - Content is delivered using **CloudFront** for faster performance.  
   - CloudFront fetches the content securely from the **S3 bucket**.

3. **Viewing Updates**  
   Any updates pushed by developers are immediately visible to users, as **Lambda** clears the CloudFront cache.

---

## S3 Bucket Policy

The following bucket policy ensures the S3 content can only be accessed via CloudFront using **Origin Access Identity (OAI)**:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E3N8IEGFMS3GGU"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-reactdemo-bucket/*"
        },
        {
            "Sid": "2",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E18DLEI46EW336"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-reactdemo-bucket/*"
        }
    ]
}

---

## Author and LinkedIn Profile:

[Abhinay Yalla](https://www.linkedin.com/in/abhinay-yalla)
