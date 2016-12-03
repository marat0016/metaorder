from django.db import models
from django import forms
from django.utils import timezone
from worker.models import Operator


STATUS_CHOICES_AND_CLASS = [
    (1,       'Обработка',            'label-default'),
    (2,       'Принят',               'label-primary'),
    (3,       'Отменён',              'label-warning'),
    (4,       'Отправлен',            'label-primary'),
    (5,       'Ждёт оплаты',          'label-info'),
    (6,       'Оплачен',              'label-success'),
    (7,       'Перевод',              'label-success'),
    (8,       'Возврат',              'label-danger'),
    (9,       'Дубликат',             'label-default'),
    (10,      'Ошибка',               'label-warning'),
]

STATUS_CHOICES = list(map(lambda x: x[0:2], STATUS_CHOICES_AND_CLASS))

class Order(models.Model):
    author = models.CharField(max_length=512, blank=False)
    email = models.EmailField(blank=False)
    text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS_CHOICES)

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



# 'NEW',      
# 'ACCEPTED', 
# 'CANCELLED',
# 'SENT',     
# 'AWAIT_PAY',
# 'PAID',     
# 'TRANSFER', 
# 'RETURN',   
# 'DUPLICATE',
# 'SPAM',     