"""
Django settings for togtourismsite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import sys
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#user model
AUTH_USER_MODEL = 'authentication.User'



# DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = True

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# if not DEBUG:
#     CSRF_TRUSTED_ORIGINS = [
#         "https://ottomantravels.com"
#     ]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new
    'django.contrib.sitemaps', # new 
    #installed app
    'sorl.thumbnail',
    'compressor',
    'django_filters',
    "crispy_forms",
    "crispy_bootstrap5",
    'django_cleanup.apps.CleanupConfig',
    'storages',
    #myapps
    'authentication',
    'blog',
    'tour',
    'mainapp',
    'newsletterapp',
    'analyticsapp',
]

SITE_ID=1
ROBOTS_USE_SCHEME_IN_HOST = True
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'mainapp.redirectmiddleware.redirect.WwwRedirectMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = 'togtourismsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'togtourismsite.wsgi.application'


DB = os.getenv("DATABASE_URL", None)

if DB is not None:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table',
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# DB = (os.getenv('DBHOST',None) and os.getenv('DBNAME',None) and os.getenv('DBUSER',None) and os.getenv('DBPASS',None))

# if DB is not None:
#     hostname = os.environ['DBHOST']
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ['DBNAME'],
#             'HOST': hostname + ".postgres.database.azure.com",
#             'USER': os.environ['DBUSER'],
#             'PASSWORD': os.environ['DBPASS'] 
#         }
#     }
#     CACHES = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#             'LOCATION': 'cache_table',
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#storage config
#STATICFILES_STORAGE = 'togtourismsite.cdn.backends.AzureStaticStorage'
#DEFAULT_FILE_STORAGE = "togtourismsite.cdn.backends.AzureMediaStorage"

USE_SPACES = os.getenv('USE_SPACES') == 'TRUE'

if USE_SPACES:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID') #DO00CMN7KUXDPNNMFHNP 
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') #dGv/hGAMwqMOoS+5RCZdbluL0wUhPZsLjjn4K55SWZQ
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME') #tourism-bucket
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = 'https://ams3.digitaloceanspaces.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    # AWS_LOCATION = 'root-dir'
    # STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    STATIC_URL = COMPRESS_URL = 'https://%s/' % (AWS_S3_ENDPOINT_URL)
    STATIC_ROOT = STATIC_URL
    STATICFILES_STORAGE = 'togtourismsite.cdn.backends.StaticStorage'
    COMPRESS_STORAGE=STATICFILES_STORAGE

    # public media settings
    # PUBLIC_MEDIA_LOCATION = 'media'
    # MEDIA_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, PUBLIC_MEDIA_LOCATION)
    MEDIA_URL = 'https://%s/' % (AWS_S3_ENDPOINT_URL)
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
    DEFAULT_FILE_STORAGE = 'togtourismsite.cdn.backends.PublicMediaStorage'
    STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
    )
    COMPRESS_PRECOMPILERS = (
        ('text/x-scss', 'django_libsass.SassCompiler'),
    )
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
    MEDIA_URL='media/'
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media_cdn')
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # other finders..
        'compressor.finders.CompressorFinder',
    )
    COMPRESS_PRECOMPILERS = (
        ('text/x-scss', 'django_libsass.SassCompiler'),
    )
    

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2,3,]


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') 
EMAIL_READY=(EMAIL_HOST_USER is not None and EMAIL_HOST_PASSWORD is not None)

if EMAIL_READY:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    #on terminal
    #python -m smtpd -n -c DebuggingServer localhost:1025

