from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def showIndex(request):
    return HttpResponse("Welcome To Function based views")

class Welcome(View):
    def get(self,request):
        return HttpResponse("Welcome To Class based views")