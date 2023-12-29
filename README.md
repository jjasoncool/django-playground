# django-playground

## Setup

```
docker-compose up -d
```

## connect mssql
- settings.py using mysql
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mariadb',
        'USER': 'root',
        'PASSWORD': '[your_password]',
        'HOST': '[db_ip]',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```
- settings.py using MSSQL
```py
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "django",
        "USER": "sa",
        "PASSWORD": "[your_password]",
        "HOST": "[db_ip]",
        "PORT": "1433",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
}
```
## create user

`python manage.py createsuperuser`

`python manage.py migrate`
