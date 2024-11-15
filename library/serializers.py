from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book"""
    class Meta:
        model = Book
        fields = ('id', 'name', 'availability', 'genre', 'user', 'author',)


class LoanSerializer(serializers.ModelSerializer):
    """Serializer for Loan"""
    class Meta:
        model = Book
        fields = ('id', 'book', 'user', 'issue_date', 'return_date',)
