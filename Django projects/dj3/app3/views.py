from django.shortcuts import render

# Create your views here.
def html1(request):
    return render(request, "index.html")


def html2(request):
    return render(request, "index1.html")