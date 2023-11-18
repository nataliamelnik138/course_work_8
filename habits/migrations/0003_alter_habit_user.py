# Generated by Django 4.2.7 on 2023-11-15 12:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0002_alter_habit_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='пользователь', to=settings.AUTH_USER_MODEL),
        ),
    ]
