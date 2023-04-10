# Generated by Django 4.1.7 on 2023-04-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0006_remove_developer_email_remove_developer_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='user',
        ),
        migrations.AddField(
            model_name='developer',
            name='username',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]