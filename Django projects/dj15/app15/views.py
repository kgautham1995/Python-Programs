from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from app15.models import StudentModel

# Create your views here.
def showIndex(request):
    res = StudentModel.objects.all()
    page_no = request.GET.get("pno")
    pg = Paginator(res, 2)
    if page_no:
        page = pg.page(page_no)
    else:
        page = pg.page(1)
    return render(request,"index.html",{"data":page})


def save_student(request):
    StudentModel(name=request.POST.get("t1"),course=request.POST.get("t2"),mobile_no=request.POST.get("t3")).save()
    return redirect('main')