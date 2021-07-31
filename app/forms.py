from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, IssueBook, User
from rest_framework.authtoken.models import Token


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['id', 'bookname', 'quantity', 'author', 'category']


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = ['studentname', 'rollno', 'book_detail']
        labels = {'studentname':'Student-Name', 'rollno':'Roll-No', 'book_detail':'Book'}
