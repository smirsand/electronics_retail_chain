from django.conf import settings
from django.db import models

from links.models import Link
from product.models import Product


class Debt(models.Model):
    """
    Модель задолженности.
    """
    duty = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    borrower = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='borrowed_debt_set',
                                 verbose_name='заемщик')
    debtor = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='owed_debt_set', verbose_name='должник')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f"Долг {self.debtor} перед {self.borrower} - {self.duty}"

    class Meta:
        verbose_name = 'долг'
        verbose_name_plural = 'долги'
