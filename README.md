# s3django
Analyzer of AWS S3 logs by Django

# How to download all S3 logs

```
pip install awscli
aws configure
...
aws s3 ls s3://BUCKETNAMEs/ --region=REGIONNAME
aws s3 cp s3://BUCKETNAME . --region=REGIONNAME --recursive
```
