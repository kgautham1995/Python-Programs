from django.http import HttpResponse
from django.shortcuts import render, redirect
from app8.models import employee

# Create your views here.
def show_home(request):
    return render(request, "Index.html")


def add_emp(request):
    return render(request, "add_emp.html")


def save(request):
    na=request.POST.get('t1')
    de=request.POST.get('t2')
    sal=request.POST.get('t3')
    employee(name=na, designation=de, salary=sal).save()
    message=" Name= " +na+ " Designation= " +de+ " Salary= " +sal
    return redirect(viewemp)


def viewemp(request):
    result=employee.objects.all()
    return render(request, 'allemp.html',{"data":result})