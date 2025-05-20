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

    username = forms.CharField(
        required=True,
        label='Username',
        help_text='Enter a unique username.',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Username is required.',
            'unique': 'This username is already taken.',
        }
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        help_text='Enter a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        }
    )

    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter a strong password.',
        error_messages={
            'required': 'Password is required.',
        }
    )

    password2 = forms.CharField(
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Re-enter your password.',
        error_messages={
            'required': 'Please confirm your password.',
        }
    )

    first_name = forms.CharField(
        required=False,
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    last_name = forms.CharField(
        required=False,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "The passwords do not match.")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



        
       


    