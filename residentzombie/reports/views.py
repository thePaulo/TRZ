from survivors.models import Survivors
from items.models import Item
from .models import Report
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

def generateReport(request):

    all_survivors=Survivors.objects.all()
    all_infected=all_survivors.filter(infected=1)
    non_infected=all_survivors.filter(infected=0)
    survivors_amount=len(all_survivors)

    infected_percent= (len(all_infected)/survivors_amount)*100 #####
    non_infected_percent= 100-infected_percent #####

    attrs = {"water_mean":0,"soup_mean":0,"medkit_mean":0,"ak_mean":0}
    attrs = calculateAttMeans(attrs,non_infected,survivors_amount) #####

    lost_points=0 #####
    for item in Item.objects.all():
        if item.owner.infected == 1:
            lost_points+=item.points

    response = {"infected_percent":infected_percent,"non_infected_percent":non_infected_percent,
                "water_mean":attrs["water_mean"],"soup_mean":attrs["soup_mean"],
                "aid_pouch_mean":attrs["medkit_mean"],
                "ak_mean":attrs["ak_mean"],"lost_points":lost_points}
    return JsonResponse(response)

def calculateAttMeans(attrs,non_infected,amnt):
    for surv in non_infected:
        attrs["water_mean"]+=surv.fiji_water
        attrs["soup_mean"]+=surv.campbell_soup
        attrs["medkit_mean"]+=surv.first_aid_pouch
        attrs["ak_mean"]+=surv.ak47

    #####
    attrs["water_mean"]=attrs["water_mean"]/amnt
    attrs["soup_mean"]=attrs["soup_mean"]/amnt
    attrs["medkit_mean"]=attrs["medkit_mean"]/amnt
    attrs["ak_mean"]=attrs["ak_mean"]/amnt

    return attrs
