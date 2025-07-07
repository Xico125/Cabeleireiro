# Cabeleireiro/settings.py
from pathlib import Path
import os
from decouple import config, Csv
import dj_database_url

# ───────────────────────────────────────────────
# BASE PATH
# ───────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────────────────────────────────────────────
# SEGURANÇA
# ───────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='insecure-secret-key-for-dev')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# ───────────────────────────────────────────────
# APPS
# ───────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps próprias
    'core',
    'cortes',
]

# ───────────────────────────────────────────────
# MIDDLEWARE
# ───────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise logo após SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ───────────────────────────────────────────────
# URLS & TEMPLATES
# ───────────────────────────────────────────────
ROOT_URLCONF = 'Cabeleireiro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Cabeleireiro.wsgi.application'

# ───────────────────────────────────────────────
# BASE DE DADOS
# ───────────────────────────────────────────────
# Usa DATABASE_URL se existir; caso contrário cai para SQLite
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False
    )
}

# ───────────────────────────────────────────────
# PASSWORD VALIDATION
# ───────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ───────────────────────────────────────────────
# I18N
# ───────────────────────────────────────────────
LANGUAGE_CODE = 'pt-pt'
TIME_ZONE = 'Europe/Lisbon'
USE_I18N = True
USE_TZ = True

# ───────────────────────────────────────────────
# STATIC & MEDIA
# ───────────────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise – comprime e faz cache‑busting
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ───────────────────────────────────────────────
# PRIMARY KEY DEFAULT
# ───────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
