# Generated by Django 5.0 on 2024-09-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0033_dragonvstigergameinvestmenttimeline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DragonvsTigerGameDumyInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('amount', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]