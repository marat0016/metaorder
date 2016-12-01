from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # todo: add reg date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Chief(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_account = models.IntegerField()
    