from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products
        }

    return render(request, 'home.html', context)

def category_page(request, pk):
    chosen_category = Category.objects.get(id=pk)
    current_products = Product.objects.filter(product_category=chosen_category)

    context = {
        'category': chosen_category,
        'products': current_products
    }

    return render(request, 'category.html', context)


def product_page(request, pk):
    chosen_product = Product.objects.get(id=pk)

    context = {
        'product': chosen_product
    }

    return render(request, 'product.html', context)



class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)


    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            # Достали данные, которые ввел пользователь
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')


            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            login(request, user)

            return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')