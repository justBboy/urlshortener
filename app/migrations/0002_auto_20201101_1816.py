# Generated by Django 3.1.2 on 2020-11-02 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='shortenedurl',
            new_name='shortenedid',
        ),
    ]