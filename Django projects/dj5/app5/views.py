from django.shortcuts import render

# Create your views here.
def show(request):
    employee1 = {"idno":101, "name":"Vijay", "salary":10000}
    employee2 = {"idno":102, "name":"Gautam", "salary":25000}
    employee3 = {"idno":103, "name":"Vikas", "salary":30000}
    return render(request, "Index.html", {"emp1":employee1,"emp2":employee2, "emp3":employee3})