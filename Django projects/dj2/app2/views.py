from django.shortcuts import render

# Create your views here.
def myhtml(request):
    return render(request,"Index.html")