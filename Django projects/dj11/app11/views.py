from django.shortcuts import render, redirect
from app11.forms import studentform

# Create your views here.

def index(request):
    return render(request, 'index.html', {'form': studentform()})
def savedet(request):
    stu = studentform(request.POST)
    if stu.is_valid():
        stu.save()
        mes="Student Saved Successfully"
        return render(request, 'index.html', {'error': mes, 'form': studentform()})
    else:
        mes = "Student already exists"
        return render(request, 'index.html',{'error':mes, 'form':studentform() })