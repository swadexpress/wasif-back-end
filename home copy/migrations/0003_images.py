# Generated by Django 3.0.7 on 2023-01-27 12:09

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230127_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=home.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
            ],
        ),
    ]
