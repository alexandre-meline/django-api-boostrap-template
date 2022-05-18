from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
     #__ Models __
     # Index models
     path('', views.dashboard, name='dashboard'),
     path('models/', views.ModelListView.as_view(), name='models'),
     # Create model
     path('new_model/', views.ModelCreateView.as_view(), name='new_model'),
     # Update model
     path('model/<pk>/edit/', views.ModelUpdateView.as_view(), name='edit_model'),
     # Details model
     path('model/<pk>/', views.ModelDetailView.as_view(), name='model'),
     # Delete model
     path('model/<pk>/delete', views.ModelDeleteView.as_view(), name='delete_model'),
     #__ Sujets __
     # Index sujets
     # Create sujet
     path('model/<int:model_id>/new_sujet/', views.SujetCreate.as_view(), name='new_sujet'),
     # Update sujet
     # Delete sujet
     #__ Texts __
     # Index texts
     # Create text
     # Update text
     # Delete text
     #__ Annotations __
     # Index annotations
     # Create annotation
     # Update annotation
     # Delete annotation
]