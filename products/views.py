import products
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.views import View
from django.urls import reverse
# Create your views here.


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products/products.html", {
            'products': products,
        })

    def post(request, products_id):
        if request.method == "POST":
            if request.user.is_authenticated:
                users = request.user
                change = request.POST.get('stock-value', None)
                product = Product.objects.get(pk=products_id)
                product.stock_available = change
                product.owners.add(users)
                product.save()
                return render(request, 'products/bought.html', {
                    'product': product,
                })
            else:
                return render(request, 'products/products.html', {
                    'message': 'User not logged in.'
                })
