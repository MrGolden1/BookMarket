from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import BookSerializer
from .models import Book

class BookViewSet(ViewSet):
    queryset = Book.objects.all()

    def list(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(item)
        return Response(serializer.data)
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=204)
    def partial_update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(instance=item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
