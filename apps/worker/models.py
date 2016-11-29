from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_time = models.DurationField()
    