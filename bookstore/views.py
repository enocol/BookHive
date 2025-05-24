from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Book, Loan, Review, Borrower
from .forms import ReviewForm, Contact, LoanForm, SigninForm, UserRegistration
from django.contrib.auth import authenticate, login


def index(request):
    query = request.GET.get('search', '')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
   
    # Get featured books
    featured_books = Book.objects.filter(featured=True)
    # Paginate the books
    paginator = Paginator(books, 6) 
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
            review_form = ReviewForm(data=request.POST)
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
        

                
                 # check if book is available
                if book.number_of_copies <= 0:
                    messages.add_message(request, messages.ERROR,'This book is currently not available for borrowing.')
                    return redirect('book_detail', book_id=book.id)
                
                
                # reduce the number of copies available
                book.number_of_copies -= 1
                # generate a collection code
                book.collection_code = f"{book.id}-{request.user.username}"


                book.save()
                loan = loan_form.save(commit=False)
                loan.book = book
                
                try:
                   loan.borrower = request.user.borrower 
                except Borrower.DoesNotExist:
                    messages.error(request, "You must be registered as a borrower to request a loan.")
                    return redirect('book_detail', book_id=book.id)
                loan.save()
                messages.add_message(
                request, messages.SUCCESS,'Loan Submitted. Colllection Code: {}'.format(book.collection_code)
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


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            review.comment = comment
            review.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, borrower=request.user.borrower).first()
    if loan:
        # Increase the number of copies available
        book.number_of_copies += 1
        book.save()
        loan.delete()
        messages.success(request, 'Book returned successfully.')
    else:
        messages.error(request, 'You have not borrowed this book.')
    return redirect('profile')

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
    return_date = Loan.objects.filter(borrower=borrower).values('return_date')

    context = {
        'loans': borrowed_books,
        'user': request.user,
        'borrower': borrower,
        'return_date': return_date,
    }

    return render(request, "bookstore/profile.html", context)


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            # Check if username or email already exists
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
                return redirect('user_registration')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists. Please choose a different one.')
                return redirect('user_registration')

            # Everything is valid, save the user
            user = form.save()

            # Create the related Borrower object
            Borrower.objects.create(
                user=user,
                email=email,
                
            )

            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('account_login')

        else:
            # Form is not valid — show errors
            messages.error(request, 'Please correct the errors below.')

    else:
        form = UserRegistration()

    return render(request, 'bookstore/user_registration.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = SigninForm()
    return render(request, 'bookstore/sign_in.html', {'form': form})


def contact(request):
    form = Contact()
    if request.method == 'POST':
       form = Contact(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Your message has been sent successfully.')
           return redirect('index')
    else:

            form = Contact()

    context   = {
        'form': form,
    }   
    return render(request, "bookstore/contact.html" , context)


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

handler404 = custom_404_view