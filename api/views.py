from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView)

from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer


# Janrlar
class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Kitoblar
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Bitta janrdagi kitoblar
class GenreBooksAPIView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(genre_id=self.kwargs['pk'])
