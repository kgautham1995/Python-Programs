from django.shortcuts import render

# Create your views here.
def showindex(request):
    data={ "nos" :[102,208,345,463,585,695,741,836,912,1050] }
    return render(request, "index.html",data)