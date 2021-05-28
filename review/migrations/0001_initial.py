# Generated by Django 3.2.2 on 2021-05-28 10:37

import cloudinary.models
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='profilepics')),
                ('bio', tinymce.models.HTMLField(blank=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='media')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
