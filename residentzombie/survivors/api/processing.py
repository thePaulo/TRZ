from django.shortcuts import get_object_or_404
from items.models import Item
from django.db import transaction

def paramsSum(param):
    dict = {}
    for c,i in enumerate(param.split()):
        dict['item{}'.format(c)] = i

    sum = 0
    for key in dict.keys():
        try:
            val = get_object_or_404(Item,id=int(dict[key])).points
        except:
            raise Exception('Id do item não foi encontrado')
        sum = sum + val
    return sum, dict

def process(param1,param2):

    sum1, dict1 =paramsSum(param1)
    sum2, dict2 =paramsSum(param2)

    if sum1 != sum2:
        raise Exception('Soma dos pontos não é igual para a troca ser efetuada')
    else:
        if checkOwner(dict1) == checkOwner(dict2):
            make_transaction(dict1,dict2)
        else :
            print('Transação não pode ser continuada')#devido a algum item em um dos dois usrs
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
    allow =True
    for key in items.keys():
        print(items[key].name)
        if items[key].owner.id == owner.id:
            pass
        else:
            allow=False
            print("troca nao permitida pois houve itens que nao pertencem ao mesmo dono")
            break
    return allow #True ou False

@transaction.atomic
def make_transaction(dict1,dict2):
    #item_dict1={}
    #item_dict2={}
    owner1=None
    owner2=None

    fitemId = (next(iter(dict1))) #id do primeiro item
    owner1 = get_object_or_404(Item,id=dict1[fitemId]).owner

    fitemId = (next(iter(dict2))) #id do primeiro item
    owner2 = get_object_or_404(Item,id=dict2[fitemId]).owner

    for key in dict1.keys():
        Item.objects.filter(id=int(dict1[key])).update(owner=owner2)
        #item_dict1[dict1[key]] = get_object_or_404(Item,id=int(dict1[key]))
        #item_dict1[dict1[key]].owner = owner2

    for key in dict2.keys():
        Item.objects.filter(id=int(dict2[key])).update(owner=owner1)
        #item_dict1[dict2[key]] = get_object_or_404(Item,id=int(dict2[key]))
        #item_dict1[dict2[key]].owner = owner
    print("Transação bem sucedida")
