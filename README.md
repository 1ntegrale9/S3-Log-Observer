AWS S3 Logs Analyzer by Django

# How to Use

```
brew install postgresql
postgres -D /usr/local/var/postgres
psql postgres
CREATE DATABASE s3log;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'Asia/Tokyo';
GRANT ALL PRIVILEGES ON DATABASE s3log TO admin;
\q
psql -U admin -d s3log

pip3 install pipenv
pipenv install
mkdir log/
aws configure
awa s3 cp s3://<KEY> ./log/ --region=<REGION> --exclude "*" --include "2018-07-19*" --recursive
pipenv run python manage.py migrate
pipenv run python manage.py runserver

ACCESS => http://127.0.0.1:8000/run

pipenv run python manage.py createsuperuser

ACCESS => http://127.0.0.1:8000/admin
```

