from django.db.models.signals import post_save
from .models import Item
from django.dispatch import receiver
from survivors.models import Survivors

@receiver(post_save,sender=Survivors)
def create_userItems(sender,instance,created,**kwargs):
    if created:
        for x in range(0,instance.fiji_water):
            Item.objects.create(name='fiji_water',points=14,owner=instance)
        for x in range(0,instance.campbell_soup):
            Item.objects.create(name='campbell_soup',points=12,owner=instance)
        for x in range(0,instance.first_aid_pouch):
            Item.objects.create(name='first_aid_pouch',points=10,owner=instance)
        for x in range(0,instance.ak47):
            Item.objects.create(name='ak47',points=8,owner=instance)
