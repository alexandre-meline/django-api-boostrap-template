from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import View
from django.urls import reverse
from . import forms, models
from accounts.models import User
import os


# Dashboard
def dashboard(request):
    return render(request, "app/dashboard.html")



# CRUD Models
class ModelListView(ListView):
    model = models.SpacyModel
    template_name = "app/models.html"

class ModelCreateView(CreateView):
    model = models.SpacyModel
    template_name = 'app/new_model.html'


    fields = ['model_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ModelCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_sujet', kwargs={'model_id': self.object.pk})


class ModelDetailView(DetailView):
    model = models.SpacyModel
    template_name = 'app/model.html'

"""class ModelUpdateView(UpdateView):
    pass

class ModelDeleteView(DeleteView):
    pass"""


# CRUD Sujets
class SujetList(ListView):
    model = models.SpacyModel
    template_name = "app/models.html"

class SujetCreate(CreateView):
    model = models.SpacySujet
    template_name = 'app/new_sujet.html'

    fields = ['sujet_name']

    def form_valid(self, form):
        form.instance.spacy_model_id = self.kwargs.get('model_id')
        return super(SujetCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('model', kwargs={'pk': self.kwargs.get('model_id')})

"""class SujetDetailView(DetailView):
    pass

class SujetUpdateView(UpdateView):
    pass

class SujetDeleteView(DeleteView):
    pass"""



# Vue formulaire création sujet
def spacy_sujet(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = forms.SpacySujetForm(request.POST or None)
    if form.is_valid():
        model_id = form.cleaned_data['spacy_model']
        new_sujet = models.SpacySujet.objects.create(
            spacy_model = models.SpacyModel.objects.get(id=model_id.id),
            sujet_name = form.cleaned_data['sujet_name']
        )

        new_sujet.save()
        os.system(f'cmd /c "python manage.py crawl -s TextSpider -u https://www.google.fr/alerts/feeds/13158359844532275904/1331939378860680853 -fk {new_sujet.id}"')
    else:
        print('je uis pas passé')

    context['form'] = form
    return render(request, "app/new_sujet.html", context)