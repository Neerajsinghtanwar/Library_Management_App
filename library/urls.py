"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    path('', views.home, name='home'),
    path('about/', views.about_us, name='aboutus'),
    path('contact/', views.contact_us, name='contactus'),
    path('login/', views.user_login, name='login'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('logout/', views.user_logout, name='logout'),
    path('addbook/', views.addbook, name='addbook'),
    path('viewbooks/', views.view_books, name='viewbooks'),
    path('delete/<int:id>', views.delete, name='deletedata'),
    path('issuebook/', views.issue_book, name='issuebook'),
    path('viewissuedbooks/', views.issued_book, name= 'viewissuedbooks'),
    path('updateissued/<int:id>', views.update_issued, name='updateissueddata'),
    path('deleteissued/<int:id>', views.delete_issued, name='deleteissueddata'),
    path('api/', include('api.urls')),
]