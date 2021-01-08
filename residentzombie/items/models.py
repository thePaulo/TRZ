from django.db import models
from survivors.models import Survivors
from django.utils.translation import gettext_lazy as _

class Item(models.Model):

    ITEM_CHOICES = [('fiji_water','Fiji Water'),('campbell_soup','Soup'),('first_aid_pouch','MedKit'),('ak47','AK47')]

    name = models.CharField(verbose_name=_("Nome"),choices=ITEM_CHOICES, max_length=255, blank=True, null=True)
    points = models.IntegerField(verbose_name=_("Pontuação"))
    owner = models.ForeignKey(Survivors,on_delete=models.CASCADE)
