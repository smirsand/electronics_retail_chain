from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    """
    Контроллер списка продуктов/товаров.
    """

    model = Product
    template_name = 'product/home.html'
    extra_context = {'title': 'Товары'}
