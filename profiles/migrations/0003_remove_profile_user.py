# Generated by Django 4.2.6 on 2023-10-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_category_tweet_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
