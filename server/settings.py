from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Change the admin site title
ADMIN_SITE_HEADER = 'Linguistics Ghana Association'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3i5xg0@&(jo135f1&3+r9b#@=9(z@r5s#t-dgo304v2v5nlsth'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
DEBUG = True

ALLOWED_HOSTS = ['app-linguisticsgh.onrender.com', '*.onrender.com', 'localhost', '127.0.0.1', 'lag-api.azurewebsites.net', 'linguisticsghana.azurewebsites.net']

CSRF_TRUSTED_ORIGINS =  ['https://' + '*.onrender.com', 'https://lag-api.azurewebsites.net', 'https://linguisticsghana.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'management',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 # ...
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'server.wsgi.application'

# connection_string = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
# if connection_string:
#     parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split()}
# else:
#     raise ValueError("AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is not set.")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }  
}

# DATABASES = {
#     'default': dj_database_url.parse("postgres://linguistics_user:54LOOBlUC4SK0tth2AeKSO5nyVkPAroI@dpg-cjg80ij37aks73b2dojg-a.oregon-postgres.render.com/linguistics")
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': parameters['dbname'],
#         'HOST': parameters['host'],
#         'USER': parameters['user'],
#         'PASSWORD': parameters['password']
#     }  
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'verceldb',
#         'HOST': 'ep-delicate-river-94174470-pooler.us-east-1.postgres.vercel-storage.com',
#         'USER': 'default',
#         'PASSWORD': 'deUzb1JZj5pE'
#     }  
# }

# password: 54LOOBlUC4SK0tth2AeKSO5nyVkPAroI;
# username: linguistics_user;
# database: linguistics;
# host: dpg-cjg80ij37aks73b2dojg-a.oregon-postgres.render.com;
# port: 5432;


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Use square brackets to create a list
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True  # Set this to True to allow all origins (not recommended for production).
CORS_ALLOW_CREDENTIALS = True  # If your API uses cookies or authentication.
CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Content-Language',
    'Content-Type',
    'Authorization',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
    'http://127.0.0.1:5501',
    'https://linguisticsghana.azurewebsites.net',
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Content-Type',
]

