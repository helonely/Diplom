from rest_framework.pagination import PageNumberPagination


class AuthorPaginator(PageNumberPagination):
    """Пагинатор для Авторов"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10


class BookPaginator(PageNumberPagination):
    """Пагинатор для книг"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10
