from django.db import models
from django.urls import reverse

# Create your models here.
# class - это таблица
# атрибуты класса - это записи(колонки) в таблице
# models.Model автоматом создает ID
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=10)

    # функция вызова url по id
    def get_url(self):
        return reverse('movie_detail', args=[self.id])

    def __str__(self):
        return f'{self.name}  - {self.rating}%'

