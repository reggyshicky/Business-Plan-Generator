from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_business_plan/', views.create_business_plan, name="create_business_plan")
]