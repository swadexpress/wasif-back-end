# Generated by Django 4.1.7 on 2023-03-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_bannerimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerimages',
            name='alt',
        ),
        migrations.AddField(
            model_name='bannerimages',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
