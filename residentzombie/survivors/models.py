from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Survivors(models.Model):
    name = models.CharField(verbose_name=_("Nome"), max_length=255, blank=True, null=True)
    age = models.IntegerField(verbose_name=_("Idade"))
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(verbose_name=_("Sexo"),choices=GENDER_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()

    NONE = 0
    ANY = 1
    GENDER_CHOICES = [(NONE, 'Não'), (ANY, 'Sim')]
