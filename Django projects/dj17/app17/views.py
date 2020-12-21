from django.shortcuts import render, redirect
from django.http import HttpResponse
from app17.form import EmployeeForm



def add_employee(request):
    return render(request,"add_employee.html",{"form":EmployeeForm()})

def save_employee(request):
    ef = EmployeeForm(request.POST,request.FILES)
    if ef.is_valid():
        ef.save()
        return HttpResponse("Data Saved Successfully")
    else:
        return render(request,"add_employee.html",{"form":ef})