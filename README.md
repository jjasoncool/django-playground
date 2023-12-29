# django-playground

## Setup

```
docker-compose up -d
```

## connect mssql
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
