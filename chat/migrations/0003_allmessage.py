# Generated by Django 4.1.6 on 2023-10-10 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0002_fruitinvestment_profile_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('other_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2p_messages_other_user_profile', to='authentication.profile')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2p_messages_user_profile', to='authentication.profile')),
            ],
        ),
    ]
