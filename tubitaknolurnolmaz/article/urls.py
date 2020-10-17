from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.index,name="index"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('article/<int:id>',views.detail,name="detail"),
]