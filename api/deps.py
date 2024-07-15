from .s3 import S3Bucket
import os

async def get_s3_client():
    bucket = S3Bucket(os.environ['AWS_BUCKET_NAME'])
    return bucket