from django.urls import path

from .views import (GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView,
                    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,
                    GenreBooksAPIView)


urlpatterns = [
    path('genres/', GenreListCreateAPIView.as_view()),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view()),
    path('genres/<int:pk>/books/', GenreBooksAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
]
