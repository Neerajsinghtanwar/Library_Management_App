from django.urls import path
from django.urls.conf import include
from api import views, auth
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('book', views.BookView, basename='book')
# router.register('issuedbook', views.IssuedBookView, basename='issuedbook')
# router.register('user', views.CreateUser, basename='user')
# router.register('staff', views.CreateStaff, basename='staff')

urlpatterns = [
    # path('', include(router.urls)),

    path('login/', auth.AuthView.as_view({'post':'login', 'get':'loginview'}), name='loginauth'),
    path('logout/', auth.AuthView.as_view({'get':'logout'}), name='logoutauth'),
    path('book/', views.BookView.as_view({'get':'list', 'post':'create'}), name='book'),
    path('book/<int:pk>', views.BookView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='bookpk'),
    path('issuedbook/', views.IssuedBookView.as_view({'get':'list', 'post':'create'}), name='issuedbook'),
    path('issuedbook/<int:pk>', views.IssuedBookView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='issuedbookpk'),
    path('user/', views.CreateUser.as_view({'get':'list', 'post':'create'}), name='user'),
    path('user/<int:pk>', views.CreateUser.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='userpk'),
    path('staff/', views.CreateStaff.as_view({'get':'list', 'post':'create'}), name='ustaff'),
    path('staff/<int:pk>', views.CreateStaff.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='staffpk'),

    # path('auth/', include('rest_framework.urls', namespace='authentication'))
]