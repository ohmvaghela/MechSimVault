from pathlib import Path
# import os
from datetime import timedelta
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!7&aq!#k$7+6vg^g)r(5#5_-@sm5&0be1anjiz7(sib@mt+0+@'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

AUTH_USER_MODEL = "siteUser.SiteUser"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders', 
    'siteUser',
    'userComments',
    'subComments',
    'simulations',
    'databaseTester',
    'tokenVerifier',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Ensure this is at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'auth-token',
    'Content-Type',
    'authorization',

]

ROOT_URLCONF = 'MechSimVault.urls'

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

WSGI_APPLICATION = 'MechSimVault.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'if0_37210959_mech_sim_vault_database',
#         'HOST':'sql103.infinityfree.com',
#         'PORT':'3306',
#         'USER':'root',
#         'PASSWORD':'giPZVPU2gwq9j7a'
#     }
# }

DATABASES = {
    # if local host
    # 'default': dj_database_url.config(default='postgresql://mech_sim_vault_user:b2s3wK1puEcY2Kvx7UCdjyA2js9saR6a@dpg-cr8svpt6l47c73bocem0-a.singapore-postgres.render.com/mech_sim_vault')
    # for render
    'default': dj_database_url.config(default='postgresql://mech_sim_vault_user:b2s3wK1puEcY2Kvx7UCdjyA2js9saR6a@dpg-cr8svpt6l47c73bocem0-a/mech_sim_vault')
}
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR/'assets'
MEDIA_ROOT = BASE_DIR/'media'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = [
    BASE_DIR/"static"
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
