# Generated by Django 4.2.3 on 2023-08-31 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('image', models.CharField(default='', max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comm', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionTimeLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default=None, max_length=2)),
                ('day_1', models.CharField(default=None, max_length=2)),
                ('day_2', models.CharField(default=None, max_length=2)),
                ('day_3', models.CharField(default=None, max_length=2)),
                ('day_4', models.CharField(default=None, max_length=2)),
                ('day_5', models.CharField(default=None, max_length=2)),
                ('day_6', models.CharField(default=None, max_length=2)),
                ('day_7', models.CharField(default=None, max_length=2)),
                ('day_8', models.CharField(default=None, max_length=2)),
                ('round_1', models.CharField(default=None, max_length=2)),
                ('round_2', models.CharField(default=None, max_length=2)),
                ('round_3', models.CharField(default=None, max_length=2)),
                ('quarter_final', models.CharField(default=None, max_length=2)),
                ('semi_final', models.CharField(default=None, max_length=2)),
                ('final', models.CharField(default=None, max_length=2)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Off', 'Off')], default='Active', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dislikes', models.ManyToManyField(blank=True, default=None, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SentGifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_admin_user_profile', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sent_user_user_profile', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('receive_user_profile', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('room_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gift_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('amount', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comm', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=500)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
        migrations.CreateModel(
            name='P2PMessageUniqueId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(default='', max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('other_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_user', to=settings.AUTH_USER_MODEL)),
                ('other_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_user_profile', to='authentication.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=home.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
        migrations.CreateModel(
            name='HostAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Pending', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('agent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_agent_user', to=settings.AUTH_USER_MODEL)),
                ('agent_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_agent_user_profile', to='authentication.profile')),
                ('join_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_join_user', to=settings.AUTH_USER_MODEL)),
                ('join_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_join_user_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_post', to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='home.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BuyCoinFromAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Pending', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('agent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_user', to=settings.AUTH_USER_MODEL)),
                ('agent_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_user_profile', to='authentication.profile')),
                ('buyer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_user', to=settings.AUTH_USER_MODEL)),
                ('buyer_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_user_profile', to='authentication.profile')),
            ],
        ),
    ]
