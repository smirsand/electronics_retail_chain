from rest_framework.pagination import PageNumberPagination


class DebtPagination(PageNumberPagination):
    page_size = 5
