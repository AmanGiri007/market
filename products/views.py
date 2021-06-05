import products
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import View
# Create your views here.


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products/products.html", {
            'products': products,
        })

    def post(self, request):
        change = request.get['stock-value']
        print(change)
