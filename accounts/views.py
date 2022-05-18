from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
import os


class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "registration/signup.html"