from .base import *
import os

# Installed Apps
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
NOSE_ARGS = [
    '--verbosity=2',                # verbose output
    '--nologcapture',               # don't output log capture
    '--with-coverage',              # activate coverage report
    '--cover-package=polls',         # coverage report will apply to packages
    '--with-spec',                  # spec style  test
    '--spec-color',
    '--with-xunit',                 # enable xunit plugin
    '--xunit-file=%s/unitests.xml' % TEST_OUTPUT_DIR,
    '--cover-xml',                   # produce XML coverage info
    '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
]


# Database
# httpp://doc.djangoproject.com/en/1.8/ref/settings/#database
# DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.mysql',
#        'NAME': os.environ.get('MYSQL_DATABASE', 'pollsdb'),
#        'USER': os.environ.get('MYSQL_USER', 'polls'),
#        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'polls123'),
#        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
#        'PORT': os.environ.get('MYSQL_PORT', '3306'),
#    }
# }
