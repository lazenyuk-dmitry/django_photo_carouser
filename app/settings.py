"""
Django settings for app project.

Using django CMS 5.0.6 and Django 6.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of Django settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/

For the list of django CMS settings and their values, see
https://docs.django-cms.org/en/release-5.0.x/reference/configuration.html
"""

import os
from pathlib import Path
import environ

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Инициализируем dotenv
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    DB_HOST=(str, '127.0.0.1'),
    DB_PORT=(int, 3306),
    USE_S3=(bool, False),
    AWS_S3_REGION_NAME=(str, 'us-east-1')
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

HEALTH_CHECK_TOKEN = env("HEALTH_CHECK_TOKEN")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Plugins
    'adminsortable2',
    'sass_processor',
    'sekizai',
    'treebeard',
    'parler',
    'filer',
    'easy_thumbnails',
    'storages',

    # Health check
    'health_check',
    # 'health_check.db',
    # 'health_check.storage',
    # 'health_check.contrib.migrations',

    # Custom apps
    'slider',
    'health',
]


SASS_PRECISION = 8
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')
SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
SASS_PROCESSOR_CUSTOM_FUNCTIONS = {}
LIBSASS_SOURCE_COMMENTS = env('DEBUG')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
DB_SSL_CA = env("SSL_CA")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {},
    }
}
if DB_SSL_CA:
    DATABASES['default']['OPTIONS']['ssl'] = {'ca': DB_SSL_CA} # /etc/ssl/certs/ca-certificates.crt


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
    # Add additional languages here
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/6.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SITE_ID = 1

# Allow admin sidebar to open admin URLs

X_FRAME_OPTIONS = 'SAMEORIGIN'

TEXT_INLINE_EDITING = True

# Add project-wide static files directory
# https://docs.djangoproject.com/en/6.0/ref/settings/#staticfiles-dirs

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Add project-wide static files directory
# https://docs.djangoproject.com/en/6.0/ref/settings/#media-root
USE_S3 = env("USE_S3")
if USE_S3:
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")

    # Настройки совместимости с Supabase
    AWS_DEFAULT_ACL = None
    AWS_S3_VERIFY = True
    AWS_S3_ADDRESSING_STYLE = "path"
    AWS_QUERYSTRING_AUTH = False

    AWS_S3_CUSTOM_DOMAIN = (
        AWS_S3_ENDPOINT_URL
        .replace("https://", "")
        .replace("/s3", f"/object/public/{AWS_STORAGE_BUCKET_NAME}")
    )

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

    THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # Для локальной разработки оставляем стандарт
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
