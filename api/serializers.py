from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'pages', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')