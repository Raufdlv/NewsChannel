from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Favorite
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


def home_page(request):
    # Достаем данные из БД
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
        context = {'form': RegForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            login(request, user)

            return redirect('/')


# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')


def add_to_favorite(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        Favorite.objects.create(
            user_id=request.user.id,
            user_product=product,
        )
        return redirect('/')
    return redirect('/')

from django.shortcuts import redirect, get_object_or_404
from .models import Favorite


def del_from_favorite(request, pk):
    if request.method == 'POST':
        Favorite.objects.filter(user_id=request.user.id, user_product_id=pk).delete()
        return redirect('/favorite')

def favorite(request):
    user_favorite = Favorite.objects.filter(user_id=request.user.id)

    context = {'favorite': user_favorite}
    return render(request, 'favorite.html', context)