from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from dj16.settings import EMAIL_HOST_USER

def showIndex(request):
    return render(request,"index.html")


def sendemail(request):
    to = request.POST.get("t1")
    subject = request.POST.get("t2")
    message = request.POST.get("t3")

    send_mail(subject,message,EMAIL_HOST_USER,[to])

    return HttpResponse("Email Sent Successfully")