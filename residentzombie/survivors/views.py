from django.http import HttpResponseRedirect
from .api.processing import process
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def displayTrades(request):


    res1= request.GET.get('s1')
    res2= request.GET.get('s2')

    process(res1,res2)

    return HttpResponseRedirect("/items")
