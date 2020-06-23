# Generated by Django 3.0.7 on 2020-06-22 23:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_city_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]