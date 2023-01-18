import boto3
import botocore
from os import environ
from scene_api.exceptions.errors import VideoUploadError

s3 = boto3.client(
    "s3",
    aws_access_key_id=environ.get("S3_KEY"),
    aws_secret_access_key=environ.get("S3_SECRET"),
)


def send_to_s3(file):
    """upload file to s3"""
    try:
        s3.upload_fileobj(
            file,
            environ.get("S3_BUCKET"),
            file.filename,
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": file.content_type,
            },
        )
    except botocore.exceptions.ClientError as error:
        # log here
        raise VideoUploadError(description=error.response["Error"]["Message"])
    return file.filename
