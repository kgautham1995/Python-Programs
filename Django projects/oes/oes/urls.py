"""oes URL Configuration

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
from django.conf.urls import url
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', views.home, name="home"),
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('home/', views.home, name='home'),
    url('base/', views.base, name='base'),
    url('profile/', views.profile, name='profile'),
    url('exam/', views.exams, name='exam'),
    url('startexam/', views.start_exam, name='startexam'),
    url('profile/(?P<user>\w+)/edit/', views.profile_update, name='profile_form'),
    url('report/', views.report, name='report'),
    url('anlysis/', views.analysis, name='result_analysis'),
    url('contact/', views.contact, name='contact'),
    url('profile/(?P<user>\w+)/detail/', views.profile_details, name='profile_detail'),
    url('logout/', views.logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

