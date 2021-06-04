"""library_management_system URL Configuration

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
from library import views
from library.middleware import authmiddleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('addbook/', authmiddleware(views.addbook), name='addbook'),
    path('viewbooks/', authmiddleware(views.view_books), name='viewbooks'),
    path('delete/<int:id>', views.delete, name='deletedata'),
    path('issuebook/', authmiddleware(views.issue_book), name='issuebook'),
    path('issuedbook/', authmiddleware(views.issued_book), name= 'issuedbook'),
    path('updateissued/<int:id>', views.update_issued, name='updateissueddata'),
    path('deleteissued/<int:id>', views.delete_issued, name='deleteissueddata'),
]
