from django.db import models

class S3AccessLog(models.Model):
    bucket_owner     = models.CharField(max_length=1024)
    bucket_name      = models.CharField(max_length=1024)
    request_datetime = models.DateTimeField()
    remote_ip        = models.CharField(max_length=1024)
    requesta         = models.CharField(max_length=1024)
    request_id       = models.CharField(max_length=1024)
    operation        = models.CharField(max_length=1024)
    request_key      = models.CharField(max_length=1024)
    request_uri      = models.CharField(max_length=1024)
    http_status      = models.IntegerField()
    error_code       = models.CharField(max_length=1024)
    bytes_sent       = models.IntegerField()
    object_size      = models.IntegerField()
    total_time       = models.IntegerField()
    turn_around_time = models.IntegerField()
    referrer         = models.CharField(max_length=1024)
    user_agent       = models.CharField(max_length=1024)
    version_id       = models.CharField(max_length=1024)

class S3AccessLog2(models.Model):
    bucket_owner     = models.CharField(max_length=1024)
    bucket_name      = models.CharField(max_length=1024)
    request_datetime = models.CharField(max_length=1024)
    remote_ip        = models.CharField(max_length=1024)
    requesta         = models.CharField(max_length=1024)
    request_id       = models.CharField(max_length=1024)
    operation        = models.CharField(max_length=1024)
    request_key      = models.CharField(max_length=1024)
    request_uri      = models.CharField(max_length=1024)
    http_status      = models.CharField(max_length=1024)
    error_code       = models.CharField(max_length=1024)
    bytes_sent       = models.CharField(max_length=1024)
    object_size      = models.CharField(max_length=1024)
    total_time       = models.CharField(max_length=1024)
    turn_around_time = models.CharField(max_length=1024)
    referrer         = models.CharField(max_length=1024)
    user_agent       = models.CharField(max_length=1024)
    version_id       = models.CharField(max_length=1024)

def CreateRecord(dataset):
    S3AccessLog2.objects.create(
        bucket_owner     = dataset['bucket_owner'],
        bucket_name      = dataset['bucket_name'],
        request_datetime = dataset['request_datetime'],
        remote_ip        = dataset['remote_ip'],
        requesta         = dataset['requesta'],
        request_id       = dataset['request_id'],
        operation        = dataset['operation'],
        request_key      = dataset['request_key'],
        request_uri      = dataset['request_uri'],
        http_status      = dataset['http_status'],
        error_code       = dataset['error_code'],
        bytes_sent       = dataset['bytes_sent'],
        object_size      = dataset['object_size'],
        total_time       = dataset['total_time'],
        turn_around_time = dataset['turn_around_time'],
        referrer         = dataset['referrer'],
        user_agent       = dataset['user_agent'],
        version_id       = dataset['version_id'],
    )
