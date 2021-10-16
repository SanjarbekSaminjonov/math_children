from django.urls import path
from . import views

urlpatterns = [
    path('noodatiy-testlar/', views.first_task, name='first_task'),
    path('noodatiy-testlar/natija', views.check, name='first_check'),
]
