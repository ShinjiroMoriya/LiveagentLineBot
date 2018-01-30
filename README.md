# Liveagent Connected on Line Bot with Celery

## Backend
- Django
- Redis
- PostgresSQL

## Requierements (pip)
- Django
- django-dotenv
- dj-database-url
- line-bot-sdk
- celery
- redis
- psycopg2
- requests
- whitenoise

```
$ pip install -r requirements.txt
```

## Overview

### Celeryの設定ファイル
```
line/celery.py
```

### Celeryのタスク処理ファイル
```
liveagent/tasks.py
```

### Liveagent接続系のファイル
```
liveagent/services.py
```

### Run Server
```
$ python manage.py runserver
```
### Run Task
```
$ celery -A line worker -l info
```
