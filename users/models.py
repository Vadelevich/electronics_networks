
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS = (
        ('active', 'Активный пользователь'),
        ('inactive', 'Не разрешенный пользователь'),
    )

    status = models.CharField(max_length=15, choices=STATUS, verbose_name='статус пользователя ',
                              default=STATUS_ACTIVE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


