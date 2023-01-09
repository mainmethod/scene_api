import boto3
from os import environ

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
    except Exception as e:
        print("S3 upload error: ", e)
        return e
    return file.filename
