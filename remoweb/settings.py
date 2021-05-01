import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'r8^d_)4zkep@uj@-86ix^a85in%b@dl)olpa*29_b3firuh%gb')
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'r8^d_)4zkep@uj@-86ix^a85in%b@dl)olpa*29_b3firuh%gb')
# DEBUG = os.getenv('DJANGO_DEBUG') == 'True'
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
# ALLOWED_HOSTS = ['django','localhost','.rederemo.org']
ALLOWED_HOSTS = ['181.214.224.242','0.0.0.0','127.0.0.1','rederemo.org','www.rederemo.org']

# if not DEBUG:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'remo.apps.RemoConfig',
    'filemanager',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware', 
    ]

SESSION_EXPIRE_SECONDS = 3600  # 1 hour

ROOT_URLCONF = 'remoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'remoweb.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
DATETIME_FORMAT = 'd-m-Y'

LANGUAGE_CODE = 'pt-br'
# TIME_ZONE = 'America/Bahia'
TIME_ZONE = 'UTC'

USE_I18N = True 
USE_L10N = False
USE_TZ = True

# SESSION AGE 5 Minutes
# SESSION_COOKIE_AGE = 30*60

# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
