from django.core.management.base import BaseCommand

from accounts.models import User

from publications.models import Publication
from random import randint
from string import printable

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.all()

        for i in range(15):
            rand_string = printable
            super_rand_string = ""
            for index in range(randint(1, 9)):
                super_rand_string += rand_string[randint(0, len(rand_string) - 1)] * randint(0, 20)

            Publication.objects.create(title=super_rand_string,
                                       body=(super_rand_string+ "\n")*randint(0, 5),
                                       image="publication/f9343018-36a4-4925-96a0-823e86079a22.jpeg",
                                       author_id=1)
