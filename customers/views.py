from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
# Create your views here.


def customer(request):
    return render(request, 'customers/customers.html', {
        'forms': CustomerForm,
    })
