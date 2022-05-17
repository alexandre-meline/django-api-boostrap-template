from django.forms import ModelForm
from . import models, forms


#Formulaire de création de model
class SpacyModelForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = models.SpacyModel

        # specify fields to be used
        fields = ["model_name"]


#Formulaire de création de sujet
class SpacySujetForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = models.SpacySujet

        # specify fields to be used
        fields = ["sujet_name"]
