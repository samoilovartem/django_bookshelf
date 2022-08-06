from django.shortcuts import render
from django.http import HttpResponse

import json


books_data = open('books.json').read()
data = json.loads(books_data)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show_book(request, id):
    single_book = []
    for book in data:
        if book.get('id') == id:
            single_book = book
    context = {'book': single_book}
    return render(request, 'books/show_book.html', context)
