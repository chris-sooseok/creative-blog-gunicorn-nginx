from storages.backends.s3boto3 import S3Boto3Storage
from config import settings

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_LOCATION
    default_acl = 'public-read'


# profile picture upload 
class ProfileMediaStorage(S3Boto3Storage):
    location = 'media/profile_pic'
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False
#
#
#class PrivateMediaStorage(S3Boto3Storage):
#    location = 'private'
#    default_acl = 'private'
#    file_overwrite = False
#    custom_domain = False

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False