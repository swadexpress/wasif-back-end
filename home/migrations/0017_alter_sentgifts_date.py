# Generated by Django 4.2 on 2023-04-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_sentgifts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentgifts',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
