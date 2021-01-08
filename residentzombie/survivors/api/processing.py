from django.shortcuts import get_object_or_404
from items.models import Item
from django.db import transaction
from django.http import Http404

#from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from django.core.exceptions import PermissionDenied

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
            #raise PermissionDenied("Id do item não foi encontrado")
            #raise Exception('Id do item não foi encontrado')
        sum = sum + val
    return sum, dict

def process(param1,param2):

    sum1, dict1 =paramsSum(param1)
    sum2, dict2 =paramsSum(param2)

    if sum1 != sum2:
        raise PermissionDenied("Soma dos pontos não é igual para a troca ser efetuada")
        #raise Exception('Soma dos pontos não é igual para a troca ser efetuada')
    else:
        if checkOwner(dict1) == checkOwner(dict2):
            make_transaction(dict1,dict2)
        else :
            raise PermissionDenied("Algum dos itens não pertencem ao mesmo sobrevivente")
            #print('Transação não pode ser continuada')#devido a algum item em um dos dois usrs
        return sum1

def checkOwner(dict):
    items={}
    for key in dict.keys():
        try:
            items[dict[key]] = get_object_or_404(Item,id=int(dict[key]))
        except:
            pass

    fitemId = (next(iter(items))) #id do primeiro item
    owner = get_object_or_404(Item,id=fitemId).owner

    if owner.infected == 1:
        #raise Response({"erro 403": "errozz"},status=403)
        raise PermissionDenied("Sobrevivente está infectado e não pode fazer trocas")
        #raise Http404("Sobrevivente está infectado e não pode fazer trocas")

    allow =True
    for key in items.keys():
        print(items[key].name)
        if items[key].owner.id == owner.id:
            pass
        else:
            allow=False
            #print("troca não permitida pois houve itens que nao pertencem ao mesmo dono")
            break
    return allow #True ou False

@transaction.atomic
def make_transaction(dict1,dict2):

    fitemId = (next(iter(dict1))) #id do primeiro item
    owner1 = get_object_or_404(Item,id=dict1[fitemId]).owner

    fitemId = (next(iter(dict2))) #id do primeiro item
    owner2 = get_object_or_404(Item,id=dict2[fitemId]).owner

    for key in dict1.keys():
        sendItem(dict1[key],owner1,owner2)
        #Item.objects.filter(id=int(dict1[key])).update(owner=owner2)

    for key in dict2.keys():
        sendItem(dict2[key],owner2,owner1)
        #Item.objects.filter(id=int(dict2[key])).update(owner=owner1)
    print("Transação bem sucedida")

def sendItem(item_id,giver,receiver):
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