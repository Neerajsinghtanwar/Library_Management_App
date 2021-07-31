from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import IssueBookForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import BookForm, IssueBookForm
from .models import Book, IssueBook, User
from django.contrib.auth.decorators import login_required
from .middlewares import underconstructionmiddleware
from app import signals

# Create your views here.

def home(request):
    if request.user.is_authenticated:   
        Group.objects.get_or_create(name='librarion')
        return render(request, 'library/home.html')
    else:    
        return render(request, 'library/index.html')


@underconstructionmiddleware
def about_us(request):
    pass


@underconstructionmiddleware
def contact_us(request):
    pass


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
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                request.session['name'] = uname
                request.session['pass'] = upass
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        fm = AuthenticationForm()
    return render(request, 'library/login.html', {'form':fm})


def admin_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                request.session['name'] = uname
                request.session['pass'] = upass
                if user.is_staff==True:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('you are not admin')
    else:
        fm = AuthenticationForm()
    return render(request, 'library/login.html', {'form':fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def addbook(request):
        form = BookForm()
        if request.method=='POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Book added successfully")
        return render(request, 'library/add_book.html', {'form': form})


@login_required
def view_books(request):
        books = Book.objects.all().order_by('id')
        return render(request, 'library/view_book.html', {'books':books})

def delete(request, id):
    if request.method == 'POST':
        pi = Book.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/viewbooks/')


@login_required
def issue_book(request):
    stuname = ""
    if request.method=='POST':
        form = IssueBookForm(request.POST)
        books = Book.objects.all()
        lst = []
        for i in books:
            i = i.id
            j = str(i)
            lst.append(j)
        stuname = form.data['studentname']
        book_name = form.data['book_detail']

        if book_name not in lst:
            messages.success(request, "*Out of stock !!")
                
        else:
            if form.is_valid():
                form.save()
                messages.success(request, "*Books issued successfuly to")
    else:
        form = IssueBookForm()          
    return render(request, 'library/issue_book.html', {'form': form, 'name':stuname})


@login_required
def issued_book(request):
    signals.notification.send(sender=IssueBook)
    books = IssueBook.objects.all()
    return render(request, 'library/issued_book.html', {'books':books})


def update_issued(request, id):
    if request.method == 'POST':
        book = IssueBook.objects.get(pk=id)
        form = IssueBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "*Data updated successfuly!!")
    else:
        book = IssueBook.objects.get(pk=id)
        form = IssueBookForm(instance=book)
    return render(request, 'library/update_issued_book.html', {'form':form})


def delete_issued(request, id):
    if request.method == 'POST':
        books = IssueBook.objects.get(pk=id)
        books.delete()
        return HttpResponseRedirect('/issuedbook/')