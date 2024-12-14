React Application Deployment Using AWS S3 and CloudFront
This README explains the Developer Workflow and User Workflow for deploying a React application using GitHub Actions, AWS S3, CloudFront, IAM, and Lambda.

Developer Workflow
The following steps describe the developer process:

Code Push:
Developers write code and push it to a GitHub repository.

GitHub Actions:

GitHub Actions automatically builds the React code.
The output is deployed to an S3 bucket.
CloudFront Integration:

Content stored in the S3 bucket is distributed via CloudFront.
This ensures fast and secure content delivery.
Lambda Cache Clearing:
When new images or files are uploaded to the S3 bucket, AWS Lambda clears the CloudFront cache to reflect updates instantly.

Workflow Diagram: Developer

User Workflow
The following steps describe how end users access the deployed application:

Accessing the Website:
Users visit the application through a domain configured with Route53.

Content Delivery:

The content is delivered via CloudFront (CDN).
CloudFront fetches the content from the S3 bucket.
Content Updates:
Users always see the latest version of the application because the cache is cleared automatically when updates are made.

Workflow Diagram: User

S3 Bucket Policy
The following S3 bucket policy ensures that content is only accessible through CloudFront with Origin Access Identity (OAI):

json
Copy code
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
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E18DLEI46EW336"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-reactdemo-bucket/*"
        }
    ]
}
Key Points:
The S3 bucket content is not publicly accessible.
Only CloudFront (using OAI) is allowed to fetch the files.
Tools and Services Used
GitHub Actions: Automates build and deployment.
AWS S3: Stores the React build files.
AWS CloudFront: Delivers content quickly via CDN.
AWS IAM: Provides secure access without root user credentials.
AWS Lambda: Clears CloudFront cache when files are updated.
Route53: Configures the custom domain for the application.
Conclusion
This project demonstrates an automated and secure workflow for deploying a React application using modern cloud services. Both developers and end-users benefit from seamless deployment and fast content delivery.

Now, when you upload this to GitHub, the images (aws_project.drawio (2).png and usrworkflow.png) will render correctly if they are placed in the same directory as the README file.

If you need any further changes or have other requirements, let me know! 🚀
