# Generated by Django 3.2 on 2021-06-15 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_rename_full_url_url_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url_hash_value',
            new_name='short_url',
        ),
    ]