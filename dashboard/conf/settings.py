import os
from mongoengine import connect

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
MONGO_DB_NAME = "test_monitoring"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_users'
    }
}

BASE_DIR = os.path.dirname(__file__)

PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

SECRET_KEY = 'slq=hz@p2wpk6yg#7wpmhkh1@*zb0)5yg#0=1t$&ug#fi%e7u)'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app.user',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.user.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "tpl"),
        ],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(PROJECT_ROOT, "app/static")

STATICFILES_DIRS = (
    # os.path.join(STATIC_ROOT, "plugins"),
    os.path.join(STATIC_ROOT, "assets"),
    os.path.join(STATIC_ROOT, "css"),
    os.path.join(STATIC_ROOT, "js"),
    # os.path.join(STATIC_ROOT, "graphs"),
    # os.path.join(STATIC_ROOT, "nodes"),
    # os.path.join(STATIC_ROOT, "index"),
    # os.path.join(STATIC_ROOT, "monitoring"),
    # os.path.join(STATIC_ROOT, "user"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

LOGIN_URL = "/login"

"""
Middleware that requires a user to be authenticated to view any page other
than LOGIN_URL. Exemptions to this requirement can optionally be specified
in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
you can copy from your urls.py).
# LOGIN_EXEMPT_URLS = []
"""
