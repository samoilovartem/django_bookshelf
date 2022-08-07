from django.shortcuts import render, get_object_or_404

from books.models import Book


def index(request):
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, 'books/index.html', context)


def show_book(request, id):
    single_book = get_object_or_404(Book, pk=id)
    context = {'book': single_book}
    return render(request, 'books/show_book.html', context)
