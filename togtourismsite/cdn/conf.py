import os
from unittest.mock import DEFAULT

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL=os.environ.get('AWS_S3_ENDPOINT_URL')
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
     "ACL": "public-read"
}
AWS_LOCATION = os.environ.get('AWS_LOCATION')
DEFAULT_FILE_STORAGE =os.environ.get('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')