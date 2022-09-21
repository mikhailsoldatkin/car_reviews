from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Country(models.Model):
    name = models.CharField('Название')

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField('Название')
    country = models.ForeignKey(
        Country,
        related_name='manufacturers',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Страна',
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField('Название')
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='cars',
        on_delete=models.CASCADE,
        verbose_name='Производитель',
    )
    start_year = models.PositiveIntegerField('Год начала выпуска')
    end_year = models.PositiveIntegerField('Год окончания выпуска')

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField('Email Автора')
    car = models.ForeignKey(
        Car,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
    )
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    text = models.TextField('Текст комментария')

    def __str__(self):
        return self.text[:15]
