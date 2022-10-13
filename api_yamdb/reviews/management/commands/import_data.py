from collections import OrderedDict

from csv import DictReader

from django.contrib.auth import get_user_model

from django.core.management import BaseCommand

from reviews.models import Category, Genre, Review, Title, Comment

from os import path

User = get_user_model()


class Command(BaseCommand):
    """Импорт данных из csv-файлов."""

    def handle(self, *args, **options):

        path_gen_part = path.join('.', 'static', 'data')
        files_models = {
            'users.csv': User,
            'category.csv': Category,
            'genre.csv': Genre,
            'titles.csv': Title,
            'review.csv': Review,
            'comments.csv': Comment
        }
        for file, model in files_models.items():
            print(f'Импорт данных из файла {file}:')
            with open(
                    path.join(path_gen_part, file),
                    encoding='utf-8',
                    newline=''
            ) as csvfile:
                reader = DictReader(csvfile)
                counter = 0
                for row in reader:
                    if not model.objects.filter(id=row['id']).exists():
                        correct_row = []
                        for key, value in row.items():
                            if key == 'genre':
                                correct_row.append(
                                    (key,
                                     Genre.objects.filter(id=value).first()
                                     )
                                )
                            if key == 'category':
                                continue
                                correct_row.append(
                                    (key,
                                     Category.objects.filter(id=value).first()
                                     )
                                )
                            elif key == 'title_id':
                                correct_row.append(
                                    ('title',
                                     Title.objects.filter(id=value).first()
                                     )
                                )
                            elif key == 'author':
                                correct_row.append(
                                    (key,
                                     User.objects.filter(id=value).first()
                                     )
                                )
                            else:
                                correct_row.append((key, value))
                        model.objects.create(**OrderedDict(correct_row))
                        counter += 1
                print(f'- импортировано {counter} записей.')
