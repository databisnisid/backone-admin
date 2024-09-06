"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#load_dotenv(dotenv_path)
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_URL
BASE_URL = str(os.getenv('BASE_URL'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
REMOTE_SELENIUM = os.getenv('REMOTE_SELENIUM', 'False').lower() in ('true', '1', 't')
SELENIUM_DOCKER = str(os.getenv('SELENIUM_DOCKER'))
PRODUCTION = os.getenv('PRODUCTION', 'False').lower() in ('true', '1', 't')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = [str(os.getenv('ALLOWED_HOSTS'))]


# Application definition

INSTALLED_APPS = [
    'landing',
    'statistic',
    'backone',
    'orbit',
    'dsc',
    'connector',
    'connection',
    'service',
    'contact',
    'project',
    'baso',
    'company',
    'notification',
    'jazzmin',
    'djmoney',
    'import_export',
    'django_crontab',
    'django_google_maps',
    'slick_reporting',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbbackup',
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': str(os.getenv('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.getenv('DB_NAME', 'db.sqlite3')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': str(os.getenv('DB_PORT')),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'id-id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "BackOne",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "BackOne",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "BackOne",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "landing/img/backone-new.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to BackOne",

    # Copyright on the footer
    "copyright": "BackOne",

    # The model admin to search from the search bar, search bar omitted if excluded
    #"search_model": "auth.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    #"topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        #{"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        #{"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        #{"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        #{"app": "books"},
    #],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    #"usermenu_links": [
    #    {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #    {"model": "auth.user"}
    #],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    #"order_with_respect_to": ["auth", "dashboard", "dashboard.chart", "data", "data.anggota", "data.keluarga", "data.wilayah"],
    "order_with_respect_to": ["statistic", "auth", "backone", 
                              #"project", "company",
                              #"service", "connection",
                              #"service", "baso", "contact", "connection",
                              "orbit",
                              ],
    # Custom links to append to app groups, keyed on app name
    #"custom_links": {
    #    "backone": [{
    #        "name": "Report",
    #        "url": BASE_URL + "sites/report/",
    #        "icon": "fas fa-file-chart-pie",
    #        "permissions": ["backone.SiteReport"]
    #    }]
    #},
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "event.event": "fas fa-user",
        "backone": "fab fa-connectdevelop",
        "backone.backone": "fas fa-sitemap",
        "project": "fas fa-tasks",
        "project.project": "fas fa-file-signature",
        "project.po": "fas fa-money-check-alt",
        "project.povendor": "fas fa-shopping-cart",
        "contact": "fas fa-address-card",
        "contact.contact": "fas fa-users",
        "company": "fas fa-city",
        "company.mycompany": "fas fa-building",
        "company.othercompany": "fas fa-hotel",
        "connection": "fas fa-network-wired",
        "connection.connectiontype": "fas fa-link",
        "connection.connectionstatus": "fas fa-plug",
        "service": "fas fa-money-bill",
        "service.servicetype": "fas fa-money-check-alt",
        "service.servicevendor": "fas fa-money-bill-wave",
        "baso": "fas fa-user",
        "baso.baso": "fas fa-user-check",
        "orbit": "fas fa-signal",
        "orbit.orbit": "fas fa-mobile-alt",
        "orbit.orbitmulti": "fas fa-mobile",
        "statistic": "fas fa-chart-pie",
        "statistic.chart": "fas fa-chart-line",
        "dsc": "fas fa-wave-square",
        "dsc.dscdpi": "fas fa-mobile"
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": 'landing/css/main.css',
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    #"dark_mode_theme": "lux",
}

# DJANGO-CRONTAB
'''
CRONJOBS = [
    ('0 6 * * *', 'statistic.cron.CRON_daily_report'),
    ('0 0 * * *', 'config.cron.dbbackup_job'),
    ('5 * * * *', 'backone.utils.update_sites_ping_status'),
]
'''

# MAP
GOOGLE_MAPS_API_KEY = str(os.getenv(('GOOGLE_MAPS_API_KEY')))
MAPS_CENTER = 'lat: -1.233982000061532, lng: 116.83728437200422'

# Upload File
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Only Django 4.0
CSRF_TRUSTED_ORIGINS = ['https://*.backone.cloud', 'https://*.127.0.0.1']

#Telegram Bot settings
TELEGRAM = {
    'bot_token': str(os.getenv('TELEGRAM_TOKEN')),
    'channel_name': 'BackOneData',
    'chat_id': '-1001760861229',
}

# CRISPY
CRISPY_TEMPLATE_PACK = 'bootstrap4'
#SLICK_REPORTING_DEFAULT_START_DATE = '01/01/2020'

# SSH Paramiko
SSH_DEFAULT_USER = str(os.getenv('SSH_DEFAULT_USER'))
SSH_DEFAULT_PASS = str(os.getenv('SSH_DEFAULT_PASS'))

NOTIF_Q_GB = int(os.getenv('NOTIF_Q_GB', 5))
NOTIF_Q_DAY = int(os.getenv('NOTIF_Q_DAY', 2))

# DSC
DSC_USERNAME = os.getenv('DSC_USERNAME')
DSC_PASSWORD = os.getenv('DSC_PASSWORD')
DSC_EMAIL_ADDRESS = os.getenv('DSC_EMAIL_ADDRESS')
DSC_EMAIL_PASSWORD = os.getenv('DSC_EMAIL_PASSWORD')
DSC_EMAIL_HOST = os.getenv('DSC_EMAIL_HOST')
DSC_URL = os.getenv('DSC_URL', 'https://dsc.telkomsel.com')

# TELKOMSAT
TELKOMSAT_USERNAME = os.getenv('TELKOMSAT_USERNAME')
TELKOMSAT_PASSWORD = os.getenv('TELKOMSAT_PASSWORD')
TELKOMSAT_TOKEN = os.getenv('TELKOMSAT_TOKEN')
TELKOMSAT_URL = os.getenv('TELKOMSAT_URL', 'https://starmon1.telkomsat.co.id')

