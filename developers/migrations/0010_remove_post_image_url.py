# Generated by Django 4.1.7 on 2023-04-09 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0009_remove_developer_username_developer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
    ]
