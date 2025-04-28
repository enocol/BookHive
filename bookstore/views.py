from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Borrower, Loan
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    books = Book.objects.all()
    print(books)
    paginator = Paginator(books, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, "bookstore/index.html", context)
