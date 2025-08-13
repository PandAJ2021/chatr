from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from .validators import validate_phone_number


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11, unique=True, validators=[validate_phone_number])
    email = models.EmailField(verbose_name="Email Address", unique=True, max_length=255)
    join_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.email