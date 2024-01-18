from django.db import models

from links.models import Link
from product.models import Product


class Purchase(models.Model):
    """
    Модель закупки товара.
    """

    product_name = models.ForeignKey(Product, related_name='purchases_with_name', on_delete=models.CASCADE,
                                     verbose_name='наименование товара')
    quantity = models.IntegerField(verbose_name='количество')
    supplier = models.ForeignKey(Link, related_name='purchases_as_supplier', on_delete=models.CASCADE,
                                 verbose_name='поставщик')
    buyer = models.ForeignKey(Link, related_name='purchases_as_buyer', on_delete=models.CASCADE,
                              verbose_name='покупатель')
    data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = 'закупка'
        verbose_name_plural = 'закупки'
