from rest_framework.serializers import ValidationError

from habits.models import Habit


class LeadTimeValidator:
    """Проверка времени на выполнение привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 120:
            raise ValidationError('Время на выполнение привычки должно быть не больше чем 120 минут')


class PeriodicityValidator:
    """Проверка периодичности выполнения в днях"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


class AssociatedHabitOrRewardValidator:
    """Проверка, что одновременно не назначено вознаграждение и связанная привычка"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        associated_habit = dict(value).get('associated_habit')
        reward = dict(value).get(self.field)
        if associated_habit is not None and reward is not None:
            raise ValidationError('Нельзя одновременно выбрать вознаграждение и связанную привычку')


class PleasurableHabitValidator:
    """Проверка, что у приятной привычки не назначено вознаграждение или связанная привычка"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        is_pleasurable = dict(value).get('is_pleasurable')
        tmp_val = dict(value).get(self.field)
        if is_pleasurable and tmp_val is not None:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class AssociatedHabitIsPleasurableHabitValidator:
    """Проверка, что связанная привычка является приятной"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        associated_habit = dict(value).get(self.field)
        habit = Habit.objects.get(pk=associated_habit.pk)

        if not habit.is_pleasurable:
            raise ValidationError('Связанная привычка не является приятной')
