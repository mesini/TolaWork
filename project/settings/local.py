"""Development settings and globals."""

import djcelery


djcelery.setup_loader()

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('django', 'django@mercycorps.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## Allowed HOsts
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['tola.work','www.mercycorps.org','www.google.com','*.github.com','www.github.com','api.github.com']

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
STATIC_URL = '/static/'

#TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
#FOR PRODUCTION USE THIS
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#FOR DEV AND TEST
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/tola-messages' # change this to a proper location
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tolawork',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'xavini', #root->xavini
        'PASSWORD': '1',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

########## END DATABASE COFIGURATION



########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

########### HACKPAD UPDATE WITH REAL CLIENT AND SECRET
HACKPAD_CLIENT_ID = ""
HACKPAD_SECRET = ""

########## GITHUB
GITHUB_AUTH_TOKEN = "b2b46138a917a1344e40d41dbb4bda2692a54200"
GITHUB_REPO_1 = "https://api.github.com/repos/mercycorps/tola"
GITHUB_REPO_2 = "https://api.github.com/repos/mercycorps/tola-activity"

########## GOOGLE AUTH UPDATE WITH REAL CLIENT AND SECRET
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "445847194486-gl2v6ud6ll65vf06vbjaslqqgejad61k.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "qAAdNMQy77Vwqgj4YgOu20f7"# LDAP stuff

########## EMAIL SETTINGS UPDATE WITH REAL CLIENT AND SECRET
LDAP_LOGIN = 'uid=pluma,ou=People,dc=system,dc=mercycorps,dc=org'
LDAP_SERVER = 'ldaps://myurl.org' # ldap dev
#LDAP_SERVER = 'ldaps://myprodurl.org' 
# ldap prodLDAP_PASSWORD = 'wickedhardtocrackpassword' 
# ldap dev#LDAP_PASSWORD = 'evenmore hardtocrackpassword1' 
# ldap prodLDAP_USER_GROUP = 'groupname'
LDAP_ADMIN_GROUP = 'groupadminname'
#ERTB_ADMIN_URL = 'https://myadminurl.org'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'toladatawork@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'toladatawork@gmail.com'
SERVER_EMAIL = "toladatawork@gmail.com"
#DEFAULT_TO_EMAIL = 'to email'

#TOLAACTIVITY & TOLATABLES API TOKEN
TOLA_ACTIVITY_TOKEN = "8b04bd2f5093ac13b881665303b190bba55a98e6"
TOLA_ACTIVITY_DEMO_TOKEN = "8b04bd2f5093ac13b881665303b190bba55a98e6"
TOLA_TABLES_IO_TOKEN = "bd43de0c16ac0400bc404c6598a6fe0e4ce73aa2"
TOLA_TABLES_DEMO_TOKEN = "bd43de0c16ac0400bc404c6598a6fe0e4ce73aa2"