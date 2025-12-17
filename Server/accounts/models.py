from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, uid, password=None, **extra_fields):
        if not uid:
            raise ValueError("User must have a UID")

        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(uid, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        FACULTY = "FACULTY", "Faculty"
        COORDINATOR = "COORDINATOR", "Course Coordinator"
        DOMAIN_MENTOR = "DOMAIN_MENTOR", "Domain Mentor"
        HOD = "HOD", "Head of Department"
        SUPERVISOR = "SUPERVISOR", "Supervisor"

    uid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=Role.choices)
    department_id = models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['name', 'role', 'department_id']

    def __str__(self):
        return f"{self.uid} - {self.name}"
