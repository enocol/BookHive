from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    cover_image = models.URLField(blank=True, null=True)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book.title} - {self.borrower.user.username}"