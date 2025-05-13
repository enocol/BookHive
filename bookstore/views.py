from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def index(request):
    query = request.GET.get('search', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
       books = Book.objects.all()
    
    # Get featured books
    featured_books = Book.objects.filter(featured=True)
    # Paginate the books
    paginator = Paginator(books, 8)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'featured_books': featured_books,
    }
    return render(request, "bookstore/index.html", context)



def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    similar_books = Book.objects.filter(category=book.category).exclude(id=book_id)[:4]  # Get 4 similar books
    context = {
        'book': book,
        'similar_books': similar_books,
    }
    return render(request, "bookstore/book_detail.html", context)


def category(request, category):
    category = Book.objects.filter(category=category)
    context = {
        
        'categories': category,
        'category_name': category[0].category if category else 'Unknown',
       
    }
    return render(request, "bookstore/category.html", context)