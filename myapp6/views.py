from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product

def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Overall quantity in db',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)

def total_in_view(request):
    products = Product.objects.all()
    total = sum(prouct.quantity for prouct in products)
    context = {
        'title': 'Overall quantity in view',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)

def total_in_template(request):
    context = {
        'title': 'Overall quantity in template',
        'products': Product
    }
    return render(request, 'myapp6/total_count.html', context)

