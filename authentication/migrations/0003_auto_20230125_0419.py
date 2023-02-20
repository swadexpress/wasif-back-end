# Generated by Django 3.0.7 on 2023-01-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230125_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='car_model',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='car_details',
            new_name='division',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/users/'),
        ),
    ]
