# Django settings for aruba (blog) project.
import os
import dj_database_url

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = os.environ.get('DJANGO_DEBUG', False)
# To enable remote debug: heroku config:add DJANGO_DEBUG=True  
# Remember to remove with heroku config:remove DJANGO_DEBUG
#TEMPLATE_DEBUG = DEBUG






dummy_from = 'mike@hotmail.com'
dummy_to = 'mike@hotmail.com'

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', dummy_from)
DEFAULT_TO_EMAIL   = os.environ.get('DEFAULT_TO_EMAIL', dummy_to)
SUPPORT_EMAIL_RCPT = os.environ.get('DEFAULT_TO_EMAIL', dummy_to)
ADMIN_EMAIL_RCPT   = os.environ.get('DEFAULT_TO_EMAIL', dummy_to) 

ADMINS = (    
    os.environ.get('DEFAULT_TO_EMAIL', dummy_to),
)

SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (('Admins', DEFAULT_TO_EMAIL), ) 

SERVER_EMAIL = DEFAULT_FROM_EMAIL   # Django (mostly logging)

MAILER = 'send_mail'
try:
    if os.environ.has_key('SENDGRID_USERNAME'):
        EMAIL_HOST = 'smtp.sendgrid.net'
        EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
        EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
except:     
    print "Unexpected sendgrid error:", sys.exc_info()







MANAGERS = ADMINS

#DATABASES = {}
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True











# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''
#MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = ''
MEDIA_URL = 'https://s3.amazonaws.com/blog-static-files/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/static/'
STATIC_URL = 'https://s3.amazonaws.com/blog-static-files/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = 'https://s3.amazonaws.com/blog-static-files/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
    #os.path.join(PROJECT_PATH, 'media'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY','over-ride locally')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','over-ride locally')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','over-ride locally')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME','over-ride locally')

DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    "django.core.context_processors.static",
#    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

INSTALLED_APPS = (
    'common',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'gunicorn',
    'mptt',
    'polls',
    'storages',
    'tagging',    
    'zinnia',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

ZINNIA_WYSIWYG = None
BITLY_LOGIN = os.environ.get('BITLY_LOGIN','over-ride locally')
BITLY_API_KEY = os.environ.get('BITLY_API_KEY','over-ride locally')
#ZINNIA_URL_SHORTENER_BACKEND = 'zinnia.url_shortener.backends.bitly'

ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia.spam_checker.backends.automattic',)
AKISMET_SECRET_API_KEY = os.environ.get('AKISMET_SECRET_API_KEY','over-ride locally')


try:
    from localsettings import *
    print 'INFO: Set to a development enviroment'
except ImportError:
    pass