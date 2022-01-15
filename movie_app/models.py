from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# class - это таблица
# атрибуты класса - это записи(колонки) в таблице
# models.Model автоматом создает ID
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=10)
    slug = models.SlugField(default='', null=False, db_index=True)

    #  функция сохранения в которой имя будет передано в slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    # функция вызова url по id
    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name}  - {self.rating}%'

# manage.py shell_plus  --print-sql
# from movie_app.models import Movie
