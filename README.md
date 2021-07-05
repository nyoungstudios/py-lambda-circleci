# Python AWS Lambda Serverless CircleCI Template

This is a simple template to setup a Python cron job as an AWS CloudFormation stack with a Lambda function and automatically deploy it with CircleCI.

It uses a couple of Serverless plugins to install the Python packages in the [requirements.txt](./requirements.txt) file to a separate Lambda layer (reducing the size of your code layer) and manage the S3 deployment bucket versioning and permissions.
