# Generated by Django 3.2.4 on 2021-06-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210612_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_project_request',
            name='project_type',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]