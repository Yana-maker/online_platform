from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings


# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя"""

    is_active = models.BooleanField(default=False, verbose_name='активный пользователь')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
