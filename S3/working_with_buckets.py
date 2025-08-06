import boto3
import pprint as pp

# s3_client = boto3.client('s3')
# s3_resource = boto3.resource('s3')

# bucket_list = s3_client.list_buckets()
# pp.pprint(bucket_list)


## Other way

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)