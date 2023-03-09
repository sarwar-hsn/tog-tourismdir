from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage 


class StaticStorage(S3Boto3Storage):
    location = 'static'
class PublicMediaStorage(S3Boto3Storage):
    location = 'media'


# from storages.backends.azure_storage import AzureStorage
# class AzureMediaStorage(AzureStorage):
#     account_name = settings.AZURE_ACCOUNT_NAME
#     account_key = settings.AZURE_STORAGE_KEY
#     azure_container = settings.AZURE_MEDIA_CONTAINER
#     expiration_secs = None
#     overwrite_files = True


# class AzureStaticStorage(AzureStorage):
#     account_name = settings.AZURE_ACCOUNT_NAME
#     account_key = settings.AZURE_STORAGE_KEY
#     azure_container = settings.AZURE_STATIC_CONTAINER
#     expiration_secs = None