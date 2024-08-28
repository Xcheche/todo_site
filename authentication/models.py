from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError("Users must have a mobile number")

        user = self.model(mobile_number=mobile_number,  **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, mobile_number, password=None,  **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(mobile_number, password,  **extra_fields)


class User(AbstractUser):
    mobile_number = models.CharField(
        max_length=11,
        null=False,
        unique=True,
        validators=[
            RegexValidator(r"^\d{11}$", "Enter a valid 11-digit mobile number.")
        ],
    )
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["email"]  # or other required fields if you have them

    objects = UserManager()

    def __str__(self):
        return self.mobile_number
