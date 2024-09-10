# Generated by Django 5.0 on 2024-09-10 13:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_profile_total_receive_coin_and_more'),
        ('chat', '0029_remove_fruitloopinvestmentwinloserecord_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot777MachineGameInvestmentWinRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_amount', models.FloatField(blank=True, default=0.0, max_length=200, null=True)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_777_machine_investment_amount_user_profile', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Slot777MachinetGameWinLoseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('win_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('rounds', models.IntegerField(blank=True, default=0, null=True)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_777_machine_game_investment_win_or_lose_user_profile', to='authentication.profile')),
            ],
        ),
    ]
