from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Book(models.Model):
    catchoice=[('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
    ]

    bookname = models.CharField(max_length=100, )
    bookid = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=catchoice, default='education')
    quantity = models.IntegerField(default=1)



    def __str__(self):
        return str(self.bookname)+"["+str(self.bookid)+']'



def get_expirydate():

    return datetime.today() + timedelta(days=15)

    
class IssueBook(models.Model):
    studentname = models.CharField(max_length=25)
    rollno = models.IntegerField()
    bookname = models.CharField(max_length=100, )
    bookid = models.PositiveIntegerField()
    issuedate = models.DateField(auto_now_add=True)
    submitdate = models.DateField(default=get_expirydate)
    
    
    def __str__(self):
        return str(self.studentname)+"["+str(self.id)+']'
    