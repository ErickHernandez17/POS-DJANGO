from django.shortcuts import render
from django.http.response import JsonResponse
from tickets.models import Items
from products.models import Products
from django.db.models import Count
from django.db.models import F
# Create your views here.

def reports_index(request):
    return render(request, 'reports/reports.html')
    
    
def get_chart(request):
    items_grouped_by_product = Items.objects.values('product').annotate(item_count=Count('id'))
    product_ids = [product['product'] for product in items_grouped_by_product]

    # Consulta para obtener los nombres de los productos correspondientes a los IDs
    products = Products.objects.filter(id__in=product_ids)

    # Crear un diccionario que mapea los IDs de producto a los nombres de producto
    product_name_dict = {product.id: product.product for product in products}

    # Crear las listas product_names_list y item_count_list
    product_names_list = [product_name_dict[product['product']] for product in items_grouped_by_product]
    item_count_list = [product['item_count'] for product in items_grouped_by_product]

    
    chart = {
        'xAxis': {
            'type': 'category',  # Corregir "category" aquí
            'data': product_names_list
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'data': item_count_list,
                'type': 'line'
            }
        ]
    }

    return JsonResponse(chart)
