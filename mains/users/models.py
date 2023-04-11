from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
import choices

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=18, unique=True)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=18)
    first_name = models.CharField(max_length=18)
    second_name = models.CharField(max_length=18)

    groups = models.ManyToManyField(
        Group,
        related_name='user_custom_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_custom_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Passenger(AbstractUser, PermissionsMixin):
    username = None
    password = None
    title = models.IntegerField(choices=choices.PERSON_TITLE)
    first_name = models.CharField(max_length=18)
    second_name = models.CharField(max_length=18)

    groups = models.ManyToManyField(
        Group,
        related_name='passenger_custom_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='passenger_custom_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
