from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save
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

    NONE = 0
    ANY = 1
    HasWater = [(NONE, 'Não'), (ANY, 'Sim')]
    HasSoup = [(NONE, 'Não'), (ANY, 'Sim')]
    HasPouch = [(NONE, 'Não'), (ANY, 'Sim')]
    HasAK = [(NONE, 'Não'), (ANY, 'Sim')]

    water = models.IntegerField(verbose_name=_("Possuí água de Fiji"),choices=HasWater)
    soup = models.IntegerField(verbose_name=_("Possuí sopa"),choices=HasSoup)
    pouch = models.IntegerField(verbose_name=_("Possuí kit"),choices=HasPouch)
    ak = models.IntegerField(verbose_name=_("Possuí AK47"),choices=HasAK)

def checkInfection(sender,instance,**kwargs):
    infected_amount = 0
    if not instance._state.adding and instance.infected == 1:
        #this is an infected update
        infected_amount = infected_amount+1
        survivors = Survivors.objects.all()
        for survivor in survivors:
            if survivor.infected == True:
                infected_amount = infected_amount + 1
    else:
        pass
    if infected_amount == 2:
        #everyone will become infected if there's enough people already infected
        survivors = Survivors.objects.all().update(infected=1)

pre_save.connect(checkInfection,sender=Survivors)
