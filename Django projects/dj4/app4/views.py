from django.shortcuts import render

# Create your views here.
def button(request):
    return render(request, "myhtml.html")