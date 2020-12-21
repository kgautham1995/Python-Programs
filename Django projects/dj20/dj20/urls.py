"""dj20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import CreateView

from app20 import views
from app20.forms import EmployeeForm
from app20.models import EmployeeModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',
         CreateView.as_view(
             template_name="index.html",
             form_class= EmployeeForm,
             success_url='/index/',
             model=EmployeeModel),
            name='main'),

   # path('login/',views.LoginCheck.as_view(),name='login_check'),
    path('validate/',views.Validateuser.as_view(),name='validate'),
]
