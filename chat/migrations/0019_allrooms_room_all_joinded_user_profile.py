# Generated by Django 4.2.6 on 2024-01-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0018_allrooms_room_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='allrooms',
            name='room_all_joinded_user_profile',
            field=models.ManyToManyField(blank=True, related_name='room_all_joinded_user_profile', to='authentication.profile'),
        ),
    ]