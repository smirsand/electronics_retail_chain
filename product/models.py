from django.db import models


class Product(models.Model):
    """
    Модель продукта.
    """

    product_name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateTimeField(verbose_name='время выхода на рынок')

    def __str__(self):
        return self.product_name, self.model

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
