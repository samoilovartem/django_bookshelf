from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='all_books'),
    path('<int:id>', views.show_book, name='single_book')
]