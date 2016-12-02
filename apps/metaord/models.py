from django.db import models
from django import forms
from django.utils import timezone
from worker.models import Operator


STATUS_CHOICES = [
    ('NEW', 'Обработка'),
    ('ACCEPTED', 'Принят'),
    ('CANCELLED', 'Отменён'),
    ('SENT', 'Отправлен'),
    ('AWAIT_PAY', 'Ждёт оплаты'),
    ('PAID', 'Оплачен'),
    ('TRANSFER', 'Перевод'),
    ('RETURN', 'Возврат'),
    ('DUPLICATE', 'Дубликат'),
    ('SPAM', 'Спам/ошибка'),
]

class Order(models.Model):
    author = models.CharField(max_length=512, blank=False)
    email = models.EmailField(blank=False)
    text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=128, choices=STATUS_CHOICES)

    def __str__(self):
        return 'author: `' + self.author + '`, text: `' + self.text + '`'

# class Order(models.Model):
#     author = models.CharField(max_length=512, blank=False) # full_name
#     phone = models.PositiveIntegerField()
#     email = models.EmailField(blank=False)
#     address = models.CharField(max_length=512)
#     text = models.TextField(blank=False)
#     post_date = models.DateTimeField(default=timezone.now)

#     amt = models.PositiveIntegerField()
#     summ = models.PositiveIntegerField()
    
#     worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
#     status = models.CharField(max_length=128)

#     def __str__(self):
#         return 'author: `' + self.author + '`, text: `' + self.text + '`'

#     class Meta:
#         ordering = ('post_date',)
