from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_time = models.DurationField(verbose_name="Время работы") # care: hardcoded in migrations
    