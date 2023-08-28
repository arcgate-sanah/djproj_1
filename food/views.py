from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list' : item_list
    }
    return render(request, 'food/index.html',context)

def item(request):
    return HttpResponse('<h1>this is an Item</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    # return HttpResponse("this is item id: %s" %item_id)
    return render(request, 'food/detail.html',context)