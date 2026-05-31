# S3-Log-Observer

Django で AWS S3 のアクセスログを取り込み、ローカルで解析するための旧試作です。

## 使い方

```bash
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
aws s3 cp s3://<KEY> ./log/ --region=<REGION> --exclude "*" --include "2018-07-19*" --recursive
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

解析画面:

```text
http://127.0.0.1:8000/run
```

管理画面:

```bash
pipenv run python manage.py createsuperuser
```

```text
http://127.0.0.1:8000/admin
```
