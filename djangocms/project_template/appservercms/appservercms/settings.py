"""
Django settings for django cms project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rk+=2d(9d87(zg1_!(u!6d)8%6pmwo-l&fet8111^&!f&=*x0q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

FILER_DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost',]

LANGUAGES = [
    ('en', 'English'), 
]

# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmsplugin_cascade', # keep before cms
    'cmsplugin_cascade.clipboard',  # optional
    'cmsplugin_cascade.extra_fields',  # optional
    'cmsplugin_cascade.sharable',  # optional
    'cmsplugin_cascade.segmentation',  # optional
    'cms',  # django CMS itself
    'djangocms_text_ckeditor',
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for JavaScript and CSS management
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'meta_mixin',
    'djangocms_blog',
    'html5up',
    # last application to finalize things
    'finalware',
)

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'appservercms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'finalware.context_processors.contextify',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]


WSGI_APPLICATION = 'appservercms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_CMSDB_USER'],
        'USER':  os.environ['POSTGRES_CMSDB_USER'],
        'PASSWORD': os.environ['POSTGRES_CMSDB_PASSWORD'],
        'HOST': os.environ['POSTGRES_CMSDB_HOST'],
        'PORT': 5432},
    'cmsdb': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_CMSDB_USER'],
        'USER':  os.environ['POSTGRES_CMSDB_USER'],
        'PASSWORD': os.environ['POSTGRES_CMSDB_PASSWORD'],
        'HOST': os.environ['POSTGRES_CMSDB_HOST'],
        'PORT': 5432},
    'appserverdb': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_APPSERVERDB_USER'],
        'USER': os.environ['POSTGRES_APPSERVERDB_USER'],
        'PASSWORD': os.environ['POSTGRES_APPSERVERDB_PASSWORD'],
        'HOST': os.environ['POSTGRES_APPSERVERDB_HOST'],
        'PORT': 5432
    }

}
#DATABASE_ROUTERS = ['apps.dbrouter.AuthRouter',]



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join("/home/cmsdb", "media/")
MEDIA_URL = "/media/"

# Add `finalware.context_processors.contextify` to your TEMPLATE_CONTEXT_PROCESSORS




CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)


CMSPLUGIN_CASCADE_PLUGINS = (
    'cmsplugin_cascade.generic',
    'cmsplugin_cascade.bootstrap3',
    'html5up',
)


CMSPLUGIN_CASCADE = {
    'alien_plugins': ('TextPlugin', 'FilerImagePlugin', ),
}


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
    ),
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'taggit': 'taggit.south_migrations',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = True

FILER_DUMP_PAYLOAD = True

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

# Add `SITE_OBJECTS_INFO_DICT` to your settings file. For example:

SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': os.environ['DJANGO_HOSTNAME'],
        'domain': os.environ['DJANGO_HOSTNAME'],
    },
}
SITE_ID = 1


# To create/update a superuser account automatically, add the following to your settings file.
# This will disable the `superuser` creation option of syncdb.

# This field is the superuser object ID. Pick something other than `1` for security reason.
SITE_SUPERUSER_ID = '987'

# This field is stored in `User.USERNAME_FIELD`. This is usually a `username` or  an `email`.
SITE_SUPERUSER_USERNAME = 'djangoadmin'

# This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = 'django@django'

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = 'djangoDJANGO'


