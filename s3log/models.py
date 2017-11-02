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
        bucket_owner     = dataset[0],
        bucket_name      = dataset[1],
        request_datetime = dataset[2],
        remote_ip        = dataset[3],
        requesta         = dataset[4],
        request_id       = dataset[5],
        operation        = dataset[6],
        request_key      = dataset[7],
        request_uri      = dataset[8],
        http_status      = dataset[9],
        error_code       = dataset[10],
        bytes_sent       = dataset[11],
        object_size      = dataset[12],
        total_time       = dataset[13],
        turn_around_time = dataset[14],
        referrer         = dataset[15],
        user_agent       = dataset[16],
        version_id       = dataset[17],
    )
