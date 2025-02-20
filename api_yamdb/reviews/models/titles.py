from django.db import models

from reviews.constants import (
    FIELD_LENGTH,
)
from reviews.models import Category, Genre

from .validators import validate_year


class Titles(models.Model):
    name = models.CharField(
        verbose_name='Название произведение',
        max_length=FIELD_LENGTH
    )
    year = models.IntegerField(
        verbose_name='Дата выхода',
        validators=(validate_year,)
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles',
        null=True,
    )
    genre = models.ManyToManyField(
        Genre, verbose_name='Жанр', related_name='titles', blank=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
