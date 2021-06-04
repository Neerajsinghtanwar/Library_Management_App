from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}

class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ['id', 'bookname', 'quantity', 'bookid', 'author', 'category']


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = models.IssueBook
        fields = ['studentname', 'rollno', 'bookname', 'bookid']
        labels = {'studentname':'Student-Name', 'rollno':'Roll-No', 'bookname':'Book-Name', 'bookid':'Book-ID'}