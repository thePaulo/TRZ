from .models import Survivors
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver

@receiver(post_save,sender=Survivors)
def checkInfection(sender,instance,created,**kwargs):
    infected_amount = 0
    #if not instance._state.adding and instance.infected == 1:
    if instance.infected == 1:
        #this is an infected update
        survivors = Survivors.objects.all()
        for survivor in survivors:
            if survivor.infected == True:
                infected_amount = infected_amount + 1
    else:
        pass
    if infected_amount == 5:
        #everyone will become infected if there's enough people already infected
        survivors = Survivors.objects.all().update(infected=1)
