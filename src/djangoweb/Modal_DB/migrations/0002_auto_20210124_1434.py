# Generated by Django 3.1.5 on 2021-01-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modal_DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maker',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pphoto',
            name='description',
            field=models.CharField(default='產品照片', max_length=50),
        ),
    ]