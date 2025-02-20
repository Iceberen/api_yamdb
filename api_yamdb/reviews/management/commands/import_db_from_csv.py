import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Titles

PATH = 'static/data/'
User = get_user_model()


class Command(BaseCommand):
    help = 'import db from csv'

    def handle(self, *args, **kwargs):
        with open(f'{PATH}/users.csv', encoding='utf-8') as users_db:
            users_data = csv.reader(users_db)
            next(users_data)

            User.objects.all().delete()

            for row in users_data:
                user = User(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6]
                )
                user.save()

        with open(f'{PATH}/category.csv', encoding="utf-8") as category_db:
            category_data = csv.reader(category_db)
            next(category_data)
            for row in category_data:
                category = Category(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )
                category.save()

        with open(f'{PATH}/genre.csv', encoding="utf-8") as genre_db:
            genre_data = csv.reader(genre_db)
            next(genre_data)
            for row in genre_data:
                genre = Genre(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )
                genre.save()

        with open(f'{PATH}/titles.csv', encoding="utf-8") as titles_db:
            titles_data = csv.reader(titles_db)
            next(titles_data)
            for row in titles_data:
                title = Titles(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=Category(pk=row[3])
                )
                title.save()

        with open(f'{PATH}/review.csv', encoding="utf-8") as review_db:
            review_data = csv.reader(review_db)
            next(review_data)
            for row in review_data:
                review = Review(
                    id=row[0],
                    title=Titles(pk=row[1]),
                    text=row[2],
                    author=User(pk=row[3]),
                    score=row[4],
                    pub_date=row[5],
                )
                review.save()

        with open(f'{PATH}/comments.csv', encoding="utf-8") as comments_db:
            comments_data = csv.reader(comments_db)
            next(comments_data)
            for row in comments_data:
                comment = Comment(
                    id=row[0],
                    review=Review(pk=row[1]),
                    text=row[2],
                    author=row[3],
                    pub_date=row[4],
                )
                comment.save()

        with open(f'{PATH}/genre_title.csv', encoding="utf-8") as gt_db:
            gt_data = csv.reader(gt_db)
            next(gt_db)
            for row in gt_data:
                title = get_object_or_404(Titles, id=row[1])
                genre = get_object_or_404(Genre, id=row[2])
                title.save()
                title.genre.add(genre)
