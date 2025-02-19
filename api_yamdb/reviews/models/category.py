from autoslug import AutoSlugField
from django.db import models

from reviews.constants import (
    FIELD_LENGTH,
)


class Category(models.Model):
    name = models.CharField(
        max_length=FIELD_LENGTH,
        verbose_name='Название категории',
    )
    slug = AutoSlugField(
        populate_from='name',
        always_update=True,
        null=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
