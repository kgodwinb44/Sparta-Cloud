# Create bucket CRUD

import boto3

s3 = boto3.client('s3')

bucket_name = s3.create_bucket(Bucket = 'data504-kyle-test-boto3', CreateBucketConfiguration)