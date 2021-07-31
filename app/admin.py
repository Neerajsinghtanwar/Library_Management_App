from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Book, IssueBook, User
from django.contrib.auth.forms import UserChangeForm

# Register your models here.

admin.site.register(Book)
admin.site.register(IssueBook)
admin.site.register(User)
