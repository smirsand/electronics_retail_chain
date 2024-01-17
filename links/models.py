from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    """
    Модель звена сети.
    """

    FACTORY = 'завод'
    IE = 'индивидуальный предприниматель'
    RETAIL = 'розничная сеть'

    STATUS_CHOICES = [
        (FACTORY, "завод"),
        (IE, "индивидуальный предприниматель"),
        (RETAIL, "розничная сеть"),
    ]
    link = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='звено сети')
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='название организации')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.link}, {self.name} - {self.email}'

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звено'
