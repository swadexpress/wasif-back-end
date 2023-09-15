# Generated by Django 4.1.6 on 2023-09-15 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_coin_alter_profile_diamond_and_more'),
        ('chat', '0010_alter_allpk_pk_request_receive_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpk',
            name='pk_request_receive_user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_receive_user_profile', to='authentication.profile'),
        ),
        migrations.AlterField(
            model_name='allpk',
            name='pk_request_sent_user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_sent_user_profile', to='authentication.profile'),
        ),
    ]
