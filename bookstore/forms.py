from django import forms
from .models import Review, Loan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'comment': 'Your Review',
            'rating': 'Rating',
        }
        help_texts = {
            'comment': 'Write your review here.',
            'rating': 'Rate the book from 1 to 5 stars.',
        }
        error_messages = {
            'comment': {
                'required': 'This field is required.',
            },
            'rating': {
                'required': 'Please select a rating.',
            },
        }

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment or comment.strip() == "":
            raise forms.ValidationError("Comment cannot be empty.")
        return comment

class LoanForm(forms.ModelForm):
   class Meta:
        model = Loan
        fields = ['return_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'return_date': 'Return Date',
        }
        help_texts = {
            'return_date': 'Select the date you plan to return the book.',
        }




class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        help_texts = {
            'username': 'Enter a unique username.',
            'first_name': 'Enter your first name.',
            'last_name': 'Enter your last name.',
            'email': 'Enter a valid email address.',
            'password1': 'Enter a strong password.',
            'password2': 'Re-enter the password for confirmation.',
        }   

        error_messages = {
            'username': {
                'required': 'This field is required.',
                'unique': 'This username is already taken.',
            },
            'email': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid email address.',
            },
            'password1': {
                'required': 'This field is required.',
                'too_common': 'This password is too common.',
                'too_similar': 'This password is too similar to your username.',
            },
            'password2': {
                'required': 'This field is required.',
                'password_mismatch': "The two password fields didn't match.",
            },
        }