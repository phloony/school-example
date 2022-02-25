from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    login = models.CharField(
        max_length=15,
        unique=True,
    )

    USERNAME_FIELD = 'login'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
