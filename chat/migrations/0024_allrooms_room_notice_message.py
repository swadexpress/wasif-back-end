# Generated by Django 4.2.6 on 2024-02-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_allrooms_room_sit_11_lock_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allrooms',
            name='room_notice_message',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
