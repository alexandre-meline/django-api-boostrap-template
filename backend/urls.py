"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
#urlpatterns Api
from rest_framework import routers
from api import views

# Setting api
# Le module suivant est celui router.urls qui fournit le routage pour notre API.
# Le router nous permet de créer les opérations suivantes :
# L'exécution d'opérations CRUD sur nos éléments est activée par le router.
# /todos/- Cette route renvoie chaque élément de notre API.
# todos/id- Renvoie un élément spécifique et c'est id.
router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]
