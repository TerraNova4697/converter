"""
DB models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Management for users."""

    def create_user(self, email, password=None, **kwargs):
        """Create and return a new user."""
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
