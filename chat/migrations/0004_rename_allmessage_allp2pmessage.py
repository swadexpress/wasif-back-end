# Generated by Django 4.1.6 on 2023-10-10 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0003_allmessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllMessage',
            new_name='AllP2PMessage',
        ),
    ]