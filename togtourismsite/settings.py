"""
Django settings for togtourismsite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#user model
AUTH_USER_MODEL = 'authentication.User'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == "1" # 1 == True

ENV_ALLOWED_HOST = os.environ.get('DJANGO_ALLOWED_HOST') or None

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1','localhost']
else:
    ALLOWED_HOSTS += [os.environ.get('DJANGO_ALLOWED_HOST')]

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
    'ckeditor',
    'django_filters',
    "crispy_forms",
    "crispy_bootstrap5",
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'robots',
    #myapps
    'authentication',
    'blog',
    'tour',
    'mainapp',
    'newsletterapp',
    'analyticsapp',
]

SITE_ID = os.environ.get('SITE_ID') or 1 
ROBOTS_SITEMAP_URLS = [
    os.environ.get('ROBOTS_SITEMAP_URLS')
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES_DB = os.environ.get("POSTGRES_DB") #database name
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") # database user password
POSTGRES_USER = os.environ.get("POSTGRES_USER") # database username
POSTGRES_HOST = os.environ.get("POSTGRES_HOST") # database host
POSTGRES_PORT = os.environ.get("POSTGRES_PORT") # database port

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_USER is not None
    and POSTGRES_HOST is not None
    and POSTGRES_PORT is not None
)

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles-cdn'
STATICFILES_DIRS = [
    BASE_DIR / "",
]

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'mediafiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': '50em',
        'width': 1200,
    },
}

THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2,3,]

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') or None
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') or None

EMAIL_READY=(
    EMAIL_HOST_USER is not None
    and EMAIL_HOST_PASSWORD is not None
)

if EMAIL_READY:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
