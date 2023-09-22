# Generated by Django 4.1.6 on 2023-09-13 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_allrooms_room_admin_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allrooms',
            name='room_admin_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_admin_profile', to='authentication.profile'),
        ),
        migrations.CreateModel(
            name='IsJoinRoomsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_coustom_unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_join_sit_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_is_join_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]