from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Borrower, Loan
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    books = Book.objects.all()
    featured_books = Book.objects.filter(featured=True)
    paginator = Paginator(books, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'featured_books': featured_books,
    }
    return render(request, "bookstore/index.html", context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, "bookstore/book_detail.html", context)
