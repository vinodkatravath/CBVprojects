"""
URL configuration for CBVProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from MyApps1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', views.HelloWorldView.as_view()),   #***add-in-last](depending on get/post request, corresponding get()/post() is executed)]
    path('home/', views.TemplateCBV.as_view()),
    path('booklistview/',views.BookListView.as_view()),
    path('companies/',views.CompanyListView.as_view()),
    path('<pk>/',views.CompanyDetailView.as_view()), #<pk> is identification for id field of your table,(primarykey=>unique+notnull



]