from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.



class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    choices = (
        ('Fiction', 'Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Romance', 'Romance'),
        
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    cover_image = CloudinaryField('image', null=True, blank=True) 
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    category = models.CharField(choices=choices, max_length=50, blank=True, null=True)
    number_of_pages = models.IntegerField(default=50)
    number_of_copies = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book.title} - {self.borrower.user.username}"