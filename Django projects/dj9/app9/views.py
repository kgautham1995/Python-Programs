from django.shortcuts import render,redirect
from app9.models import employee
from django.contrib import messages

def showIndex(request):
    return render(request,"index.html")

def add_employee(request):
    return render(request,"add_employee.html")

def save_emp(request):
    id = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    # Query inserting a record into database
    # 1 object means 1 record(1 row)
    employee(idno=id,name=na,salary=sal).save()

    messages.success(request,"Registration is Successful")
    return redirect('main')

    #return render(request,"index.html",{"message":"Registration is Successful"})


def view_all(request):
    # Query to read all records from DB
    res = employee.objects.all()
    return render(request,"allEmployees.html",{"data":res})


def delete_employee(request):
    no = request.GET.get("no")
    # Query to delete 1 record from DB
    employee.objects.filter(idno=no).delete()
    return redirect('view_all')


def show_update(request):
    no = request.GET.get("t1")
    # Query to read 1 record from DB
    result = employee.objects.get(idno=no)
    return render(request,"update.html",{"data":result})


def update_emp(request):
    no = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    # Query to update a record
    employee.objects.filter(idno=no).update(name=na,salary=sal)
    return redirect('view_all')