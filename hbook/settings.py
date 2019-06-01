import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = os.environ.get('DEBUG', 'True') == 'True' # environment vars are strings. "convert" to boolean. lol, Python
SECRET_KEY = os.environ.get('SECRET_KEY', '12312312312312123123123123')

ALLOWED_HOSTS = [
  # TODO: add your Google Cloud Project-ID here
    'hbook-001.appspot.com', # must add the app engine (project-id) domain here
    '127.0.0.1', # for local testing 
    'server.hbook.ml',
    '*'
]

# Application definition
STATIC_URL = os.environ.get('STATIC_URL', '/static/') # /static/ if DEBUG else Google Cloud bucket url
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'hbook-bucket')
STATICFILES_DIRS = [
  # TODO: configure the name and path to your development static directory
    os.path.join(BASE_DIR, 'static'), # static directory (in the top level directory) for local testing
]
# print('-------\n', STATICFILES_DIRS, STATIC_ROOT, STATIC_URL, DEBUG, sep='\n')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # Libraries used
    'rest_framework',
    'knox',
    # Inside apps
    'hbook.users',
    'hbook.users.school',
    'hbook.ev'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hbook.urls'

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

WSGI_APPLICATION = 'hbook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
      'PORT': os.environ.get('DB_PORT', 5432),
      'NAME': os.environ.get('DB_NAME', 'hbook-db'),
      'USER': os.environ.get('DB_USER', 'ray-db-user'),
      'PASSWORD': os.environ.get('DB_PASSWORD', '5ks5bTuErwVh4Sm')
    }
}
''' # For local if needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
''' '''



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'knox.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://localhost:8000',
    'https://hashblog.herokuapp.com'
)

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
