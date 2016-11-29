from django.db import models
from django.utils import timezone


class Order(models.Model):
    author = models.CharField(max_length=512)
    email = models.EmailField()
    text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=128)

    def __str__(self):
        return 'author: `' + self.author + '`, text: `' + self.text + '`'
