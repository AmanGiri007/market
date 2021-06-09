from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .login_forms import CustomerForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .register_forms import RegisterForm

# Create your views here.


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('products'))
        forms = CustomerForm()
        return render(request, 'customers/login.html', {
            'forms': forms,
        })

    def post(self, request):
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            password = forms.cleaned_data['password']
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                logged = f"{name} has logged in."
                return render(request, 'customers/login.html', {
                    'log': logged,
                })
            message = "User not found. Please Login again or create a new account."
            return render(request, 'customers/login.html', {
                'no_user': message,
            })
        return render(request, 'customers/login.html', {
            'no_user': 'Invalid Try Again',
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('products')
        form = RegisterForm()
        return render(request, 'customers/register.html', {
            'forms': form,
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=name, email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect(reverse('products'))
        return HttpResponse('Form not filled properly')


class UserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            users = request.user
            user_name = users.username.capitalize()
            products = users.products.all()
            total_rate = 0
            for i in range(len(products)):
                total_rate += products[i].product_rate
            # print(total_rate)
            return render(request, 'customers/customers_bucket.html', {
                'products': products,
                'rates': total_rate,
                'users': user_name,
            })
        return HttpResponseRedirect(reverse('products'))
