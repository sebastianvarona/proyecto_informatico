from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diagnosis/<int:diagnosis_id>/', views.diagnosis_detail, name='diagnosis_detail'),
]
