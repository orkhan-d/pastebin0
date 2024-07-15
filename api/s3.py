from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import aioboto3
import aiofiles

class S3Bucket:
    def __init__(self, bucket: str):
        self.session = aioboto3.Session()
        self.bucket = bucket

    async def get_file(self, filename: str) -> bytes:
        async with self.session.client("s3") as client: # type: ignore
            response = await client.get_object(Bucket=self.bucket, Key=filename)
            return await response['Body'].read()
        
    async def upload_file(self, filename: str, data: bytes):
        async with self.session.client('s3') as client: # type: ignore
            await client.put_object(Bucket=self.bucket, Key=filename, Body=data)