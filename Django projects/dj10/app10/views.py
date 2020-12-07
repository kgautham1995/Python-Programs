from django.shortcuts import render,redirect
from app10.models import CourseModel,StudentModel
from django.db.utils import IntegrityError

def showIndex(request):
    return render(request,"index.html")

def add_course(request):
    result = CourseModel.objects.all()
    return render(request,"add_course.html",{"data":result})

def save_course(request):
    name = request.POST.get("c1")
    fee = request.POST.get("c2")
    try:
        CourseModel(course_name=name,course_fee=fee).save()
        return redirect("add_course")
    except IntegrityError:
        res = CourseModel.objects.all()
        mes = "Course Name is Taken"
        return render(request, "add_course.html", {"data": res,"error":mes})


def add_student(request):
    c = CourseModel.objects.all()
    r = StudentModel.objects.all()
    return render(request,"add_student.html",{"all_course":c,"data":r})


def save_student(request):
    name = request.POST.get("s1")
    contact = request.POST.get("s2")
    courses = request.POST.getlist("s3")

    sm = StudentModel(student_name=name,student_contactno=contact)
    sm.save()
    sm.student_courses.set(courses)

    return redirect('add_student')