# Generated by Django 2.1.7 on 2019-02-26 04:26

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('p3erest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipee',
            new_name='Recipe',
        ),
    ]
