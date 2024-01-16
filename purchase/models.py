from django.db import models

from links.models import Link
from product.models import Product


class Purchase(models.Model):
    """
    Модель закупки товара.
    """

    product_name = models.ForeignKey(Product, related_name='purchases_with_name', on_delete=models.CASCADE,
                                     verbose_name='наименование товара')
    quantity = models.IntegerField(verbose_name='количество товара')
    hierarchy = models.IntegerField(default=0, verbose_name='иерархия')
    supplier = models.ForeignKey(Link, limit_choices_to={'link': Link.FACTORY, 'hierarchy': 0}, related_name='purchases_as_supplier', on_delete=models.CASCADE,
                                 verbose_name='поставщик товара')
    buyer = models.ForeignKey(Link, related_name='purchases_as_buyer', on_delete=models.CASCADE,
                              verbose_name='покупатель товара')
    data = models.DateTimeField(verbose_name='дата создания')

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = 'закупка'
        verbose_name_plural = 'закупки'
