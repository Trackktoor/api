# Generated by Django 3.2 on 2021-06-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.URLField(unique=True)),
                ('url_hash_value', models.CharField(max_length=16)),
                ('clicks', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='URL_hash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_use', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(max_length=155)),
                ('if_mobile', models.BooleanField()),
                ('url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shortner.url')),
            ],
        ),
    ]
