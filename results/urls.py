from django.urls import path
from . import views


urlpatterns = [
    path('', views.results_dashboard, name='results_dashboard'),
    path('json', views.search_pupil_result),
]
