from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from app20.models import EmployeeModel


class Validateuser(View):
    def post(self,request):
        cno = request.POST.get("username")
        upass = request.POST.get("password")
        try:
            data = EmployeeModel.objects.get(contactno=cno,password=upass)
            return render(request,'welcome.html',{"data":data})
        except EmployeeModel.DoesNotExist:
            return  redirect('main')

