# Generated by Django 4.1.6 on 2023-09-12 00:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimages',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
