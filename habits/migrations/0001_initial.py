# Generated by Django 4.2.7 on 2023-11-15 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='место')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время')),
                ('periodicity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('once every 2 days', 'Через день'), ('once every 3 days', 'Один раз в 3 дня'), ('once every 4 days', 'Один раз в 4 дня'), ('once every 5 days', 'Один раз в 5 дней'), ('once every 6 days', 'Один раз в 6 дней')], default='daily', max_length=17, verbose_name='периодичность')),
                ('action', models.CharField(max_length=150, verbose_name='действие')),
                ('is_pleasurable', models.BooleanField(blank=True, default=False, null=True, verbose_name='приятная привычка')),
                ('reward', models.IntegerField(blank=True, null=True, verbose_name='вознаграждение')),
                ('lead_time', models.IntegerField(verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(blank=True, default=False, null=True, verbose_name='публичня привычка')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]