from django.db import models
from survivors.models import Survivors
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from random import randint

# Create your models here.
class Item(models.Model):

    ITEM_CHOICES = [('Fiji Water','Fiji Water'),('Soup','Soup'),('MedKit','MedKit'),('AK47','AK47')]

    name = models.CharField(verbose_name=_("Nome"),choices=ITEM_CHOICES, max_length=255, blank=True, null=True)
    points = models.IntegerField(verbose_name=_("Pontuação"))
    owner = models.ForeignKey(Survivors,on_delete=models.CASCADE)

def spawn(minimum_items,name,points,owner):
    for x in range(minimum_items+randint(0,10)):
        Item.objects.create(name=name,points=points,owner=owner)

def create_userItems(sender,instance,created,**kwargs):
    minimum_items=5
    if created:
        if instance.water == 1:
            spawn(minimum_items,'Fiji Water',14,instance)
        if instance.soup == 1:
            spawn(minimum_items,'Soup',12,instance)
        if instance.ak == 1:
            spawn(minimum_items,'AK47',10,instance)
        if instance.pouch == 1:
            spawn(minimum_items,'First Aid Pouch',8,instance)
        #Item.objects.create()

#post_save.connect(create_userItems,sender=Survivors)
