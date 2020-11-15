from django.db import models


class Client(models.Model):
    name=models.CharField('Ім`я',max_length=50)
    surname=models.CharField('Прізвище',max_length=100)
    email=models.CharField('Імейл',max_length=50)
    mobile=models.CharField('Телефон',max_length=20)

    def __str__(self):
        return self.name



