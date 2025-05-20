from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib import messages  # Optional: For feedback
from .models import Book, Loan
from django.core.paginator import Paginator
from .forms import ReviewForm
from .forms import LoanForm
from django.contrib.auth.models import User
from .models import Borrower
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration


def index(request):
    query = request.GET.get('search', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
       books = Book.objects.all()
    
    # Get featured books
    featured_books = Book.objects.filter(featured=True)
    # Paginate the books
    paginator = Paginator(books, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'featured_books': featured_books,
        'query': query,
        
    }
    return render(request, "bookstore/index.html", context)




def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    similar_books = Book.objects.filter(category=book.category).exclude(id=book_id)[:4]
    reviews = book.reviews.all()

    # Default forms (for POST or in case of invalid POST)
    review_form = ReviewForm()
    loan_form = LoanForm()

    if request.method == 'POST':
        if 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                messages.add_message(
        request, messages.SUCCESS,
        'Your review has been submitted successfully.'
    )
                return redirect('book_detail', book_id=book.id)

        elif 'submit_loan' in request.POST:
            loan_form = LoanForm(data=request.POST)
            if loan_form.is_valid():

               
                # check if user has already borrowed the book
                if Loan.objects.filter(book=book, borrower=request.user.borrower).exists():
                    messages.add_message(request, messages.ERROR,'You have already borrowed this book. Please return it before borrowing again.'
    
    )
                    return redirect('book_detail', book_id=book.id)
                
                 # check if book has been borrowed
                if book.number_of_copies <= 0:
                    messages.add_message(request, messages.ERROR,'This book is currently not available for borrowing.')
                    return redirect('book_detail', book_id=book.id)
                
                
                # reduce the number of copies available
                book.number_of_copies -= 1
                book.save()
                loan = loan_form.save(commit=False)
                loan.book = book
                # loan.borrower = request.user.borrower
                try:
                   loan.borrower = request.user.borrower  # Will raise if borrower doesn't exist
                except Borrower.DoesNotExist:
                    messages.error(request, "You must be registered as a borrower to request a loan.")
                    return redirect('book_detail', book_id=book.id)
                loan.save()
                messages.add_message(
                request, messages.SUCCESS,'You have successfully borrowed the book. Please return it by the due date.'
    )
                return redirect('book_detail', book_id=book.id)
            else:
                messages.add_message(request, messages.ERROR,'There was an error with your loan request. Please try again.'
    )
                return render(request, 'bookstore/book_detail.html', {
                    'book': book,
                    'similar_books': similar_books,
                    'reviews': reviews,
                    'review_form': review_form,
                    'loan_form': loan_form,
                })

    context = {
        'book': book,
        'similar_books': similar_books,
        'reviews': reviews,
        'review_form': review_form,
        'loan_form': loan_form,
    }

    return render(request, 'bookstore/book_detail.html', context)



def category(request, category):
    category = Book.objects.filter(category=category)
    context = {
        
        'categories': category,
        'category_name': category[0].category if category else 'Unknown',
       
    }
    return render(request, "bookstore/category.html", context)

def about(request):
    return render(request, "bookstore/about.html")

@login_required
def profile(request):
    borrower = Borrower.objects.get(user=request.user)
    borrowed_books = Book.objects.filter(loan__borrower=borrower).distinct()

    context = {
        'loans': borrowed_books,
        'user': request.user,
    }

    return render(request, "bookstore/profile.html", context)


def user_registration(request):
    if request.method == 'POST':
        # Get the form data
        form  = UserRegistration(data=request.POST)
        user = User()
        if form.is_valid():
            # Save the user
            user = form.save()
          
            # Create a Borrower instance
            borrower = Borrower.objects.create(
                user=user,
                email=form.cleaned_data['email'],
               
            )

            borrower.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('account_login')
        else:
            print('Form is not valid:', form.errors)
            messages.error(request, 'Please correct the errors below.')
        
    
    
    context = {
        'form': UserRegistration(),
        'messages': messages,
    }

    return render(request, "bookstore/user_registration.html", context)


