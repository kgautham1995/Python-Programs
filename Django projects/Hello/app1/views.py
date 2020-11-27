from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    message="Hello Everyone \n Welcome to programming with gautam"
    return HttpResponse(message)
