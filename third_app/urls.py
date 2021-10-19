from django.urls import path
from . import views

urlpatterns = [
    path('kreativ-fikrlash/', views.third_task, name='third_task'),
    path('kreativ-fikrlash/natija', views.check, name='third_check'),
]
