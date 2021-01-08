from .models import Survivors
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save,sender=Survivors)
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
