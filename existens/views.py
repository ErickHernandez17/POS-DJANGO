from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from inventories.models import Inventories
# Create your views here.

def existens_list_view(request):
    query = request.GET.get('q')  
    if query:
        existens = Inventories.objects.select_related('product').filter(state=True, quantity__gt=0,product__product__icontains=query).all()
    else:
        existens = Inventories.objects.select_related('product').filter(state=True, quantity__gt=0).all()
    return render(request, 'existens/existens.html', {'existens':existens, 'query':query})

