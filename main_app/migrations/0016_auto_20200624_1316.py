# Generated by Django 3.0.7 on 2020-06-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20200623_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]