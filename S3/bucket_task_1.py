import boto3
import pandas as pd
import io
import json

class S3Handler:
    def __init__(self):
        self.bucket_name = 'data-eng-resources'
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')

    def list_objects_with_resource(self, prefix="python/"):
        bucket = self.s3_resource.Bucket(self.bucket_name)
        for obj in bucket.objects.all():
            if prefix in obj.key:
                print(obj.key)

    def list_objects_with_client(self, prefix="python/"):
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        for obj in response.get('Contents', []):
            print(obj['Key'])

    def get_object_content(self, key):
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        content = response['Body'].read()
        print(content)

    def download_csv_to_dataframe(self, key, save_path=None):
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        content = response['Body'].read()
        df = pd.read_table(io.BytesIO(content), sep=',')
        if save_path:
            df.to_csv(save_path, index=False)
        return df

    def upload_json(self, key, data: dict):
        json_data = json.dumps(data)
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=json_data,
            ContentType='application/json'
        )

    def upload_file(self, file_path, key):
        self.s3_client.upload_file(file_path, self.bucket_name, key)
        print(f'Uploaded {file_path} to {self.bucket_name}/{key}')


def main():
    handler = S3Handler()
    print(handler.get_object_content('python/happiness-2019.csv'))
    
if __name__ == "__main__":
    main()
    
