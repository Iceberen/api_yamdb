from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from reviews.constants import (
    FIELD_LENGTH,
    MAX_SCORE,
    MIN_SCORE,
    TEXT_LIMIT,
)
from reviews.models import (
    Titles,
)

User = get_user_model()


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
