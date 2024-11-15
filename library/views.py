from django.utils import timezone
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Author, Book, Loan
from library.paginators import BookPaginator, AuthorPaginator
from library.permissions import IsModerator
from library.serializers import BookSerializer, AuthorSerializer, LoanSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""CRUD for authors"""


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsModerator,]


class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]


class AuthorRetrieveApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsModerator]


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsModerator]


"""CRUD for books"""


class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsModerator]


class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'genre', 'user', 'availability', 'author']


class BookRetrieveApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsModerator]


class BookDestroyApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsModerator]


"""CRUD for loans"""


class LoanCreateApiView(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsModerator]


class LoanListApiView(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user', 'issue_date', 'return_date']


class LoanRetrieveApiView(RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanUpdateApiView(UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsModerator]


class LoanDestroyApiView(DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsModerator]


class ReturnBookApiView(APIView):
    permission_classes = [IsModerator]

    def post(self, request, loan_id):
        try:
            loan = Loan.objects.get(id=loan_id)
            if loan.return_date:
                return Response({"error": "Книгу уже вернули"}, status=status.HTTP_400_BAD_REQUEST)

            loan.return_date = timezone.now()
            loan.save()
            return Response({"message": "Книгу успешно вернули"}, status=status.HTTP_200_OK)
        except Loan.DoesNotExist:
            return Response({"error": "Выдача книги не найдена"}, status=status.HTTP_404_NOT_FOUND)
