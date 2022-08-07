from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

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
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        return context


# def show_book(request, id):
#     single_book = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': single_book,
#                'reviews': reviews}
#     return render(request, 'books/show_book.html', context)


def review(request, id):
    review_content = request.POST['review']
    new_review = Review(content=review_content, book_id=id)
    new_review.save()
    return redirect('/book')
