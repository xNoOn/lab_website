from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import os


class StaticStorage(S3Boto3Storage):
    bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    location = 'static'


class MediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    location = 'images'