from rest_framework.pagination import PageNumberPagination


class PurchasePagination(PageNumberPagination):
    page_size = 5
