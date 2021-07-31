from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from .managers import StaffManager, UsersManager, IssuedBookManager
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class User(AbstractUser):
    user_type_data=(("H.O.D","H.O.D"),("Staff","Staff"),("Student","Student"))
    user_type=models.CharField(choices=user_type_data,max_length=10)
    objects = UserManager()
    staff = StaffManager()
    users = UsersManager()
    

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.user_type = "H.O.D"
        elif self.is_staff:
            self.user_type = "Staff"
        else:
            self.user_type = "Student"
        super(User, self).save(*args, **kwargs)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    catchoice=[('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
    ]

    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=catchoice, default='education')
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return str(self.bookname)+"["+str(self.id)+']'

def expiry_date():
    return datetime.today().date() + timedelta(days=15)

class IssueBook(models.Model):
    id = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=25)
    rollno = models.IntegerField()
    book_detail = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuedate = models.DateField(auto_now_add=True)
    submitdate = models.DateField()
    fine = models.IntegerField(default=0)
    objects = models.Manager()
    issued = IssuedBookManager()
    
    def __str__(self):
        return str(self.studentname)+"["+str(self.id)+']'
    
    def save(self, *args, **kwargs):
        self.submitdate = expiry_date()
        return super(IssueBook, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        