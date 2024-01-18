from django.db import models

from links.models import Link


class Debt(models.Model):
    """
    Модель задолженности.
    """
    duty = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг')
    borrower = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='borrowed_debt_set', verbose_name='заемщик')
    debtor = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='owed_debt_set', verbose_name='должник')

    def __str__(self):
        return f"{self.duty}"

    class Meta:
        verbose_name = 'долг'
        verbose_name_plural = 'долги'
