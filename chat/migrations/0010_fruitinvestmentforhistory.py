# Generated by Django 4.2.6 on 2024-01-02 17:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0009_fruitinvestmenttimeline_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitInvestmentForHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment', models.CharField(blank=True, default=None, max_length=20000, null=True)),
                ('profile_data', models.CharField(blank=True, default=None, max_length=20000, null=True)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruit_investment_for_history_user_profile', to='authentication.profile')),
            ],
        ),
    ]
