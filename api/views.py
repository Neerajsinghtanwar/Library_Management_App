from .serializers import BookSerializer, IssueBookSerializer, UserSerializer
from rest_framework import viewsets, status
from app.models import Book, IssueBook, User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from app import signals
from .permission import MyPermission
from django.contrib.auth.hashers import make_password
from .pagination import MyPagination


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = ['^bookname']

    pagination_class = MyPagination


class IssuedBookView(viewsets.ModelViewSet):
    
    queryset = IssueBook.issued.all()
    serializer_class = IssueBookSerializer
    
    permission_classes = [IsAuthenticated]

    search_fields = ['^rollno']

    def list(self, request, *args, **kwargs):
        signals.notification.send(sender=IssueBook)
        return super().list(request, *args, **kwargs)
        
    
class CreateUser(viewsets.ModelViewSet):
    queryset = User.users.all()
    serializer_class = UserSerializer

    permission_classes = [MyPermission]

    search_fields = ['^name']
  
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():        
            p = make_password(serializer.validated_data['password'])
            User.users.create(first_name=serializer.validated_data['first_name'], last_name=serializer.validated_data['last_name'], email=serializer.validated_data['email'], username=serializer.validated_data['username'], password=p)
            return Response({'msg':'Created Successfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class CreateStaff(viewsets.ModelViewSet):
    queryset = User.staff.all()
    serializer_class = UserSerializer

    permission_classes = [MyPermission]

    search_fields = ['^name']
  
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():                   
            p = make_password(serializer.validated_data['password'])
            User.staff.create(first_name=serializer.validated_data['first_name'], last_name=serializer.validated_data['last_name'], email=serializer.validated_data['email'], username=serializer.validated_data['username'], password=p, is_staff=True)
            return Response({'msg':'Created Successfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)