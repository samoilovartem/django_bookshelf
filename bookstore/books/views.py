from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from books.forms import ReviewForm
from books.models import Book, Review


class BookListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/show_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.all()
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
        return context


def review(request, id):
    if request.user.is_authenticated:
        new_review = Review(book_id=id,
                            user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=new_review)
        if form.is_valid():
            form.save()
    return redirect(f'/books/{id}')


def get_author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'books': books}
    return render(request, 'books/index.html', context)
