from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='пользователь', blank=True, null=True)
    place = models.CharField(max_length=150, verbose_name='место', blank=True, null=True)
    time = models.TimeField(verbose_name='время', blank=True, null=True)
    periodicity = models.IntegerField(verbose_name='периодичность в днях', default=1)
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasurable = models.BooleanField(default=False, verbose_name='приятная привычка', blank=True, null=True)
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                         verbose_name='связанная привычка')
    reward = models.CharField(blank=True, null=True, verbose_name='вознаграждение')
    lead_time = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публичня привычка', blank=True, null=True)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
