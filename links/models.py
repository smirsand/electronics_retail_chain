from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    """
    Родительская модель звена сети.
    """
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='наименование')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.name}'

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звено'


class Factory(Link):
    """
    Модель завода.
    """

    def __str__(self):
        return f'{self.email}, {self.name}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class IE(Link):
    """
    Модель индивидуального предпринимателя.
    """

    def __str__(self):
        return f'{self.email}, {self.name}'

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'


class Retail(Link):
    """
    Модель розничной сети.
    """

    def __str__(self):
        return f'{self.email}, {self.name}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'
