from django.contrib.auth import models
from app.models import IssueBook, Book, User
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = "__all__"
        read_only_fields = ['fine', 'submitdate',]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True, required=True, help_text='Enter your password', style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=True, help_text='Enter your password again', style={'input_type': 'password', 'placeholder': 'Confirm-Password'})

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
            'password',
            'confirm_password',
            'groups',
            'user_permissions',
        ]
        read_only_fields = ['id', 'is_staff', 'is_superuser', 'user_permissions', 'groups']

    def validate(self, data):
        p1 = data.get('password')
        p2 = data.get('confirm_password')
        if p1 != p2:
            raise serializers.ValidationError({'msg': 'password does not match', 'password':p1, 'confirm_password':p2})
        return data
