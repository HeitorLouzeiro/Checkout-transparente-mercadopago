from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('processpayment/', views.processpayment, name='processpayment'),
    path('pending/', views.resultpayment, name='resultpayment'),

]
