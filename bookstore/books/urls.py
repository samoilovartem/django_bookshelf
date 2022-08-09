from django.urls import path
from books.views import BookListView, BookDetailView, review, get_author


urlpatterns = [
    path('', BookListView.as_view(), name='all_books'),
    path('<int:pk>', BookDetailView.as_view(), name='single_book'),
    path('<int:id>/review', review, name='review'),
    path('<str:author>', get_author, name='book_author')
]