# Generated by Django 4.1.6 on 2023-09-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_coin_alter_profile_diamond_and_more'),
        ('chat', '0020_allrooms_room_mute_mic_user_profile_banded_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allrooms',
            name='room_sup_admin_profile',
            field=models.ManyToManyField(blank=True, related_name='room_sup_admin_profile', to='authentication.profile'),
        ),
    ]