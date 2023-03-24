from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage 


class StaticStorage(S3Boto3Storage):
    location = 'static'
class PublicMediaStorage(S3Boto3Storage):
    location = 'media'