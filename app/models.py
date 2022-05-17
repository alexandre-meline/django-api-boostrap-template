from django.db import models
from django.conf import settings

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SpacyModel(BaseModel):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    model_name = models.CharField(
        max_length=100)

    def __str__(self):
        return self.model_name

class SpacySujet(BaseModel):
    spacy_model = models.ForeignKey(
        to=SpacyModel,
        on_delete=models.CASCADE
        )
    sujet_name = models.CharField(
        max_length=100)

    def __str__(self):
        return self.sujet_name


class SpacyText(BaseModel):
    spacy_sujet = models.ForeignKey(
        to=SpacySujet,
        on_delete=models.CASCADE
    )
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text

class SpacyAnnotation(BaseModel):
    spacy_model = models.ForeignKey(
        to=SpacyModel,
        on_delete=models.CASCADE
    )
    annotation = models.CharField(max_length=100)

    def __str__(self):
        return self.annotation

class SpacyScore(BaseModel):
    spacy_model = models.ForeignKey(
        to=SpacyModel,
        on_delete=models.CASCADE
    )
    score = models.IntegerField()

    def __str__(self):
        return self.score

class SpacyDataset(BaseModel):
    spacy_model = models.ForeignKey(
        to=SpacyModel,
        on_delete=models.CASCADE
    )
    dataset = models.TextField()

    def __str__(self):
        return self.dataset