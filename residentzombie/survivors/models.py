from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Survivors(models.Model):
    name = models.CharField(verbose_name=_("Nome"), max_length=255, blank=True, null=True)
    age = models.IntegerField(verbose_name=_("Idade"))
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Homem'), (GENDER_FEMALE, 'Mulher')]
    gender = models.IntegerField(verbose_name=_("Sexo"),choices=GENDER_CHOICES)
    latitude = models.FloatField(validators=[MaxValueValidator(90),MinValueValidator(-90)])
    longitude = models.FloatField(validators=[MaxValueValidator(180),MinValueValidator(-180)])

    INFECTED_CHOICES = [(0,'Não'),(1,'Sim')]
    infected = models.IntegerField(verbose_name=_("Infectado"),choices=INFECTED_CHOICES,default=0)

    '''NONE = 0
    ANY = 1
    HasWater = [(NONE, 'Não'), (ANY, 'Sim')]
    HasSoup = [(NONE, 'Não'), (ANY, 'Sim')]
    HasPouch = [(NONE, 'Não'), (ANY, 'Sim')]
    HasAK = [(NONE, 'Não'), (ANY, 'Sim')]'''

    fiji_water = models.IntegerField(verbose_name=_("Possuí água de Fiji"),validators=[MinValueValidator(0)])
    campbell_soup = models.IntegerField(verbose_name=_("Possuí sopa"),validators=[MinValueValidator(0)])
    first_aid_pouch = models.IntegerField(verbose_name=_("Possuí Med kit"),validators=[MinValueValidator(0)])
    ak47 = models.IntegerField(verbose_name=_("Possuí AK47"),validators=[MinValueValidator(0)])
