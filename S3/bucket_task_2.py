import pandas as pd
import boto3
import io

class S3Handler:
    def __init__(self):
        self.bucket_name = 'data-eng-resources'
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')
    
    def download_file_in_bucket(self, key):
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        content = response['Body'].read()
        df = pd.read_table(io.BytesIO(content), sep=',')
        df.to_csv('S3/csv/kyle-fish-data.csv')
        print(f"File {key} has been downloaded")
    
    def transform_data_to_upload(self, file, key):
        df = pd.read_csv('S3/csv/kyle-fish-data.csv')
        df_avg = df.groupby('Species').mean().reset_index()
        df_avg.to_csv('S3/csv/kyle-transformed-fish.csv')
        print(f"Transformed file has been created")
        
        self.s3_client.upload_file(file, self.bucket_name, key)
        print(f"Uploaded {file} to {self.bucket_name}/{key}")
        
def main():
    handler = S3Handler()
    print(handler.transform_data_to_upload())
    
if __name__ == "main":
    main()
        