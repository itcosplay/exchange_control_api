from django.db import models


class BotUser(models.Model):
    PERMISSION_LEVEL_NAMES = (
        ('A', 'Admin'),
        ('E', 'Executor'),
        ('S', 'Secretary'),
        ('U', 'Unknown'),
    )

    username = models.CharField(
        max_length=100,
        verbose_name='Пользователь'
    )

    telegram_id = models.IntegerField()

    permission_level = models.CharField(
        max_length=50,
        verbose_name='Уровень прав',
        choices=PERMISSION_LEVEL_NAMES,
        default='U'
    )
