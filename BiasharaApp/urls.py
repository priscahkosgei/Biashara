
from django.contrib import admin
from django.urls import path
from BiasharaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('add/', views.add, name='add'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('services/', views.services, name='services'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),







]
