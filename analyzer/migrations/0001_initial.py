# Generated by Django 2.2.2 on 2019-06-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='S3AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_owner', models.CharField(max_length=1024)),
                ('bucket_name', models.CharField(max_length=1024)),
                ('request_datetime', models.CharField(max_length=1024)),
                ('remote_ip', models.CharField(max_length=1024)),
                ('requesta', models.CharField(max_length=1024)),
                ('request_id', models.CharField(max_length=1024)),
                ('operation', models.CharField(max_length=1024)),
                ('request_key', models.CharField(max_length=2048)),
                ('request_uri', models.CharField(max_length=2048)),
                ('http_status', models.CharField(max_length=1024)),
                ('error_code', models.CharField(max_length=1024)),
                ('bytes_sent', models.CharField(max_length=1024)),
                ('object_size', models.CharField(max_length=1024)),
                ('total_time', models.CharField(max_length=1024)),
                ('turn_around_time', models.CharField(max_length=1024)),
                ('referrer', models.CharField(max_length=1024)),
                ('user_agent', models.CharField(max_length=1024)),
                ('version_id', models.CharField(max_length=1024)),
            ],
        ),
    ]