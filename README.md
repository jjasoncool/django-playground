# django-playground

## Setup

```
docker-compose up -d
```

## connect db
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

## create user

`python manage.py createsuperuser`

`python manage.py migrate`
