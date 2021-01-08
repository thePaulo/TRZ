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

    res1= request.GET.get('s1')
    res2= request.GET.get('s2')

    process(res1,res2)
    '''name = Item.objects.filter(owner=survivor).first().name

    setattr(survivor,name,4)
    survivor.save()'''
    '''
    zz = Item.objects.filter(owner=survivor).first()
    name = zz.name


    print(getattr(survivor,name))
    current = getattr(survivor,name)
    current = current-1
    print(current)
    '''

    return render(request,"file.html",{"eu":survivor,"items":my_items})
