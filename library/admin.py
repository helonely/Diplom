from django.contrib import admin

from library.models import Author, Book, Loan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'availability', 'author', 'genre')
    list_filter = ('id', 'name', 'availability', 'author', 'genre')
    search_fields = ('id', 'name', 'availability', 'author', 'genre')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'issue_date', 'return_date')
    list_filter = ('id', 'book', 'user', 'issue_date', 'return_date')
    search_fields = ('id', 'book', 'user', 'issue_date', 'return_date')
