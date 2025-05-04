from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Borrower, Loan
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    query = request.GET.get('search', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
       books = Book.objects.all()
    
    # Get featured books
    # Assuming you have a field 'featured' in your Book model
    featured_books = Book.objects.filter(featured=True)
    # Paginate the books
    # Assuming you want to show 6 books per page
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

def category(request, category):
    category = Book.objects.filter(category=category)
    featured_books = Book.objects.filter(featured=True)
   
    context = {
        
        'categories': category,
        'featured_books': featured_books,
    }
    return render(request, "bookstore/category.html", context)