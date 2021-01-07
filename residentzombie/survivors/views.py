from django.shortcuts import get_object_or_404,render
from .models import Survivors
from items.models import Item
from django.http import HttpResponseRedirect

from django.forms import inlineformset_factory
from .api.processing import process

# Create your views here.

def displayTrades(request,survivor_id):
    survivor = get_object_or_404(Survivors,id=survivor_id)
    my_items = Item.objects.filter(owner=survivor)

    #TradeForm = inlineformset_factory(Survivors,Item,fields=('name',))
    #formset = TradeForm(queryset=Item.objects.none(),instance=survivor)
    #my_form = TradeForm(survivor)

    res1= request.GET.get('s1')
    res2= request.GET.get('s2')

    process(res1,res2)



    #print(sum)
    #return render(request,"file.html",{"formset":formset})
    return render(request,"file.html",{"eu":survivor,"items":my_items})



'''
def processTrades(request,survivor_id):


    res= request.GET.getlist('cars',False)
    for z in res:
        print(checkPoints(z))
    return render(request,"file.html")

def checkPoints(str):
    item = Item.objects.filter(name=str).first()
    return item.points
'''
