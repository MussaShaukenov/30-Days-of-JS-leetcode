# Generated by Django 4.2.6 on 2023-11-25 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_communitycategory_alter_community_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='category',
        ),
    ]
