from django.contrib import admin
from .models import Book, IssueBook

# Register your models here.
admin.site.register(Book)
admin.site.register(IssueBook)