from django.db import models

from product.models import Product


class Link(models.Model):
    """
    Модель звена сети.
    """
    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.ImageField(max_length=150, verbose_name='номер дома')

    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return self.email, self.country

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звено'


class Factory(Link):
    """
    Модель завода.
    """

    def __str__(self):
        return self.email, self.country

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Retail(Link):
    """
    Модель розничной сети.
    """
    supplier = models.ForeignKey(Factory, blank=True, on_delete=models.CASCADE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг перед поставщиком')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.email, self.country

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class IE(Link):
    """
    Модель индивидуального предпринимателя.
    """
    supplier = models.ForeignKey(Factory, blank=True, on_delete=models.CASCADE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг перед поставщиком')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.email, self.country

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'
