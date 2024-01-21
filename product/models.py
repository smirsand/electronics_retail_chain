from django.db import models

from links.models import Link

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """
    Модель продукта.
    """

    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.IntegerField(verbose_name='количество')
    release_date = models.DateTimeField(verbose_name='время выхода на рынок')
    supplier = models.ForeignKey(Link, limit_choices_to={'link': Link.FACTORY},
                                 related_name='manufacturer_products', on_delete=models.CASCADE,
                                 verbose_name='поставщик')
    owner_link = models.ForeignKey(Link, limit_choices_to={'link': Link.FACTORY}, on_delete=models.CASCADE,
                                   verbose_name='владелец')

    hierarchy = models.IntegerField(default=0, verbose_name='иерархия')

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
