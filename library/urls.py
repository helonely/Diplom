from django.urls import path

from library.apps import LibraryConfig
from library.views import BookListApiView, BookRetrieveApiView, BookCreateApiView, BookDestroyApiView, \
    BookUpdateApiView, AuthorListApiView, AuthorRetrieveApiView, AuthorDestroyApiView, AuthorCreateApiView, \
    AuthorUpdateApiView, LoanCreateApiView, LoanListApiView, LoanRetrieveApiView, LoanUpdateApiView, \
    LoanDestroyApiView, ReturnBookApiView

app_name = LibraryConfig.name


urlpatterns = [
    path('books/', BookListApiView.as_view(), name='books_list'),
    path('book/<int:pk>/', BookRetrieveApiView.as_view(), name='book_retrieve'),
    path('book/create/', BookCreateApiView.as_view(), name='book_create'),
    path('book/<int:pk>/delete/', BookDestroyApiView.as_view(), name='book_delete'),
    path('book/<int:pk>/update/', BookUpdateApiView.as_view(), name='book_update'),

    path('loan/create/', LoanCreateApiView.as_view(), name='loan_create'),
    path('loans/', LoanListApiView.as_view(), name='loan_list'),
    path('loan/<int:pk>/', LoanRetrieveApiView.as_view(), name='loan_retrieve'),
    path('loan/<int:pk>/update/', LoanUpdateApiView.as_view(), name='loan_update'),
    path('loan/<int:pk>/delete/', LoanDestroyApiView.as_view(), name='loan_delete'),
    path('loan/<int:pk>/return/', ReturnBookApiView.as_view(), name='loan_return'),

    path('authors/', AuthorListApiView.as_view(), name='authors_list'),
    path('author/<int:pk>/', AuthorRetrieveApiView.as_view(), name='author_retrieve'),
    path('author/create/', AuthorCreateApiView.as_view(), name='author_create'),
    path('author/<int:pk>/delete/', AuthorDestroyApiView.as_view(), name='author_delete'),
    path('author/<int:pk>/update/', AuthorUpdateApiView.as_view(), name='author_update'),
]