from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter_data/', views.enter_data, name='enter_data'),
]