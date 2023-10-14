# Generated by Django 4.1.6 on 2023-09-27 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitInvestmentTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('end_time', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IsJoinRoomsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_coustom_unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_join_sit_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_join_join_uniq_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_is_join_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FruitInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment', models.CharField(blank=True, default=None, max_length=20000, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruit_investment_user_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AllSentedGifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_coustom_unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gift_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gift_amount', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gift_receive_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_receive_user', to=settings.AUTH_USER_MODEL)),
                ('gift_receive_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_receive_user_profile', to='authentication.profile')),
                ('gift_sent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_sent_user', to=settings.AUTH_USER_MODEL)),
                ('gift_sent_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_sent_user_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AllRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_coustom_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_welcome_message', models.CharField(blank=True, default='Welcome', max_length=200, null=True)),
                ('room_tag', models.CharField(blank=True, default='Welcome', max_length=200, null=True)),
                ('room_image', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_media_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_user_can_join', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_lock', models.BooleanField(blank=True, default=False, null=True)),
                ('room_password', models.CharField(blank=True, default='57706', max_length=200, null=True)),
                ('room_sit_1_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_1_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_1_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_2_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_2_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_2_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_3_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_3_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_3_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_4_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_4_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_4_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_5_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_5_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_5_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_6_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_6_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_6_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_7_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_7_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_7_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_8_lock_position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_8_password', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_sit_8_mic_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_admin_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_admin_profile', to='authentication.profile')),
                ('room_admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_admin_user', to=settings.AUTH_USER_MODEL)),
                ('room_mute_mic_user_profile_banded_list', models.ManyToManyField(blank=True, related_name='room_mute_mic_user_profile_banded_list', to='authentication.profile')),
                ('room_mute_mic_user_profile_list', models.ManyToManyField(blank=True, related_name='room_mute_mic_user_profile_list', to='authentication.profile')),
                ('room_sup_admin_profile', models.ManyToManyField(blank=True, related_name='room_sup_admin_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AllPK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_request_sent_user_balance', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('pk_request_receive_user_balance', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('pk_unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_coustom_unique_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pk_time', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pk_start_time', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pk_end_time', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pk_request_receive_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_receive_user', to=settings.AUTH_USER_MODEL)),
                ('pk_request_receive_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_receive_user_profile', to='authentication.profile')),
                ('pk_request_sent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_sent_user', to=settings.AUTH_USER_MODEL)),
                ('pk_request_sent_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk_request_sent_user_profile', to='authentication.profile')),
            ],
        ),
    ]