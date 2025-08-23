from pathlib import Path
import os
import dj_database_url


# مسیر پایه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت
# SECRET_KEY = 'django-insecure-)1=dmv_wabqhcp@3*f@#c4*o!q2q)be1s4%ocx()mtd$%&oyy$'

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")

DEBUG = False
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]  # بعدا میتونی محدودش کنی به آدرس رندر

# اپ‌ها
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'accounts',
        'widget_tweaks',

]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # اضافه شد
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL root
ROOT_URLCONF = 'todoproject.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # مسیر templates اصلی پروژه
        'APP_DIRS': True,  # قالب‌های داخل هر app هم شناسایی شوند
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'todoproject.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
# STATIC_URL = 'static/'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# dpg-d2kum9buibrs73emaj70-a
# in:postgresql://todolist_db_zbco_user:CDI42LmHiVJjHt6qeAs2X7DgdFXc5pW8@dpg-d2kum9buibrs73emaj70-a/todolist_db_zbco