from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс нового пользователя.
    """

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='smirsand@mail.ru',
            first_name='Иван',
            last_name='Иванов',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456')
        user.save()
