from autoslug import AutoSlugField

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import validate_year


from reviews.constants import (
    FIELD_LENGTH,
    MAX_SCORE,
    MIN_SCORE,
    TEXT_LIMIT,
)

User = get_user_model()


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


class Genre(models.Model):
    name = models.CharField(
        max_length=FIELD_LENGTH,
        verbose_name='Название жанра',
    )
    slug = AutoSlugField(
        populate_from='name',
        always_update=True,
        null=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(
        verbose_name='Название произведение', max_length=FIELD_LENGTH
    )
    year = models.IntegerField(
        verbose_name='Дата выхода', validators=(validate_year,)
    )
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True
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


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='произведение',
    )
    text = models.CharField(max_length=FIELD_LENGTH)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор',
    )
    score = models.IntegerField(
        'рейтинг',
        validators=(
            MinValueValidator(MIN_SCORE),
            MaxValueValidator(MAX_SCORE),
        ),
        error_messages={
            'validators': f'Оценка от {MIN_SCORE} до {MAX_SCORE}!'
        },
    )
    pub_date = models.DateTimeField(
        'дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'title',
                    'author',
                ),
                name='unique review',
            )
        ]
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:TEXT_LIMIT]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='отзыв',
    )
    text = models.CharField('текст комментария', max_length=FIELD_LENGTH)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор',
    )
    pub_date = models.DateTimeField(
        'дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:TEXT_LIMIT]
