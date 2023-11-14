from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(
        upload_to='users/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    telegram_chat_id = models.CharField(max_length=35, verbose_name='ID чата Telegram', blank=True, null=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
