from django.db import models


class S3AccessLog(models.Model):
    bucket_owner = models.CharField(max_length=64)
    bucket_name = models.CharField(max_length=128)
    request_datetime = models.DurationField()
    remote_ip = models.GenericIPAddressField()
    requesta = models.CharField(max_length=256, blank=True, null=True)
    request_id = models.CharField(max_length=16, unique=True)
    operation = models.CharField(max_length=128)
    request_key = models.CharField(max_length=2048)
    request_uri = models.CharField(max_length=2048)
    http_status = models.PositiveSmallIntegerField(blank=True, null=True)
    error_code = models.CharField(max_length=1024, blank=True, null=True)
    bytes_sent = models.PositiveSmallIntegerField(blank=True, null=True)
    object_size = models.PositiveIntegerField(blank=True, null=True)
    total_time = models.PositiveSmallIntegerField(blank=True, null=True)
    turn_around_time = models.PositiveSmallIntegerField(blank=True, null=True)
    referrer = models.CharField(max_length=1024, blank=True, null=True)
    user_agent = models.CharField(max_length=128, blank=True, null=True)
    version_id = models.CharField(max_length=128, blank=True, null=True)


def CreateRecord(dataset):
    S3AccessLog.objects.create(
        bucket_owner=dataset[0],
        bucket_name=dataset[1],
        request_datetime=dataset[2],
        remote_ip=dataset[3],
        requesta=dataset[4],
        request_id=dataset[5],
        operation=dataset[6],
        request_key=dataset[7],
        request_uri=dataset[8],
        http_status=dataset[9],
        error_code=dataset[10],
        bytes_sent=dataset[11],
        object_size=dataset[12],
        total_time=dataset[13],
        turn_around_time=dataset[14],
        referrer=dataset[15],
        user_agent=dataset[16],
        version_id=dataset[17],
    )
