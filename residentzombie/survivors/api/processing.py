from django.shortcuts import get_object_or_404
from items.models import Item
from django.db import transaction
from django.http import Http404
from django.core.exceptions import PermissionDenied

#sums up the informed points inside the items ids from s1 and s2 and stores each of it in a item's dictionary
def paramsSum(param):
    dict = {}
    for c,i in enumerate(param.split()):
        dict['item{}'.format(c)] = i


    sum = 0
    for key in dict.keys():
        try:
            val = get_object_or_404(Item,id=int(dict[key])).points
        except:
            raise Http404("Id do item fornecido não foi encontrado")
        sum = sum + val
    return sum, dict

#returns the sum from each survivor's item points and checks its ownership, receives the two get parameters from the "/trading" url
def process(param1,param2):

    sum1, dict1 =paramsSum(param1)
    sum2, dict2 =paramsSum(param2)

    if sum1 != sum2:
        raise PermissionDenied("Soma dos pontos não é igual para a troca ser efetuada")
    else:
        if checkOwner(dict1) == checkOwner(dict2):
            make_transaction(dict1,dict2)
        else :
            raise PermissionDenied("Algum dos itens não pertencem ao mesmo sobrevivente")
        return sum1

#checks if the survivor is infected or not, and it checks its ownership.Its param is a dict from a survivor's items. returns (True = owns, False = doesent own )
def checkOwner(dict):
    items={}
    for key in dict.keys():
        try:
            items[dict[key]] = get_object_or_404(Item,id=int(dict[key]))
        except:
            pass

    fitemId = (next(iter(items)))
    owner = get_object_or_404(Item,id=fitemId).owner

    if owner.infected == 1:
        raise PermissionDenied("Sobrevivente está infectado e não pode fazer trocas")

    allow =True
    for key in items.keys():
        if items[key].owner.id == owner.id:
            pass
        else:
            allow=False
            break
    return allow #True ou False

#makes the trade between two survivors, its params are the item dictionaries from each survivor
@transaction.atomic
def make_transaction(dict1,dict2):

    fitemId = (next(iter(dict1))) 
    owner1 = get_object_or_404(Item,id=dict1[fitemId]).owner

    fitemId = (next(iter(dict2))) 
    owner2 = get_object_or_404(Item,id=dict2[fitemId]).owner

    for key in dict1.keys():
        sendItem(dict1[key],owner1,owner2)

    for key in dict2.keys():
        sendItem(dict2[key],owner2,owner1)
    print("Transação bem sucedida")

#adjusts the ownership and item amount from each survivor    
def sendItem(item_id,giver,receiver):
        try:
            with transaction.atomic():
                item_name = Item.objects.filter(id=item_id).first().name
                item_amount = getattr(giver,item_name)
                item_amount -= 1
                setattr(giver,item_name,item_amount)
                item_amount = getattr(receiver,item_name)
                item_amount += 1
                setattr(receiver,item_name,item_amount)
                giver.save()
                receiver.save()
                Item.objects.filter(id=item_id).update(owner=receiver)
        except:
            raise Exception()
