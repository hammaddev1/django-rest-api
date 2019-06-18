from rest_framework.pagination import PageNumberPagination

class SmallSetPgination(PageNumberPagination):
  page_size = 3