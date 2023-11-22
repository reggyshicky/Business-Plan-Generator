from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_business_plan/', views.create_business_plan, name="create_business_plan"),
<<<<<<< HEAD
    path('thank_you/', views.thank_you, name='thank_you'),
=======
    path('export_to_pdf/', views.export_to_pdf, name='export_to_pdf')
>>>>>>> master
]