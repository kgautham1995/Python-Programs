from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request, "Index.html")


def display(request):
    # fetching data from index.html
    i=request.POST.get("a1")
    n=request.POST.get("a2")
    m=request.POST.get("a3")
    print(i,n,m)
    message=" IDNO= " +i+ " Name= " +n+ " Marks= "+m
    return HttpResponse(message)