from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def check(request):
    if request.method == "POST":
        name = request.POST.get("t2")
        x="I am post method"
        y=x+name
        return HttpResponse(y)
    else:
        name = request.GET.get("t1")
        return HttpResponse("I am GET Button")