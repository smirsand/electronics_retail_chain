from django.db import models

from links.models import Factory

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """
    Модель продукта.
    """
    product_name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateTimeField(verbose_name='время выхода на рынок')
    manufacturer = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='производитель')

    def __str__(self):
        return f"{self.product_name} {self.model}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
