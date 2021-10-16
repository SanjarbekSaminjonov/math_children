from django.urls import path
from . import views

urlpatterns = [
    path('mantiqiy-savollar/', views.second_task, name='second_task'),
    path('mantiqiy-savollar/check',
         views.second_check, name='second_check'),
]
