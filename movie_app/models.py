from django.db import models

# Create your models here.
# class - это таблица
# атрибуты класса - это записи(колонки) в таблице
# models.Model автоматом создает ID
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
