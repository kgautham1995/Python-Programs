from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    msg='''<html>
                <body bgcolor=grey>
                <h1> Welcome to Programming with Gautam Youtube channel</h1>
                </body>
            </html>'''
    return HttpResponse(msg)