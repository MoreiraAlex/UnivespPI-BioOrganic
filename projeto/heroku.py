import environ
from .settings import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}

SITE_ID = env.int('SITE_ID', 1)

#AMAZOM S3
#################################################################################
AWS_ACCESS_KEY_ID = 'AKIAVMZ77YHHMR6DZTWR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'biorganic'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#################################################################################