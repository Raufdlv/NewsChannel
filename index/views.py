from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def home_page(request):
    # Достаем данные из БД
    categories = Category.objects.all()
    products = Product.objects.all()

    # Отправляем данные на фронт
    context = {
        'categories': categories,
        'products': products
        }

    return render(request, 'home.html', context)


def category_page(request, pk):
    # Достаем данные из БД
    chosen_category = Category.objects.get(id=pk)
    current_products = Product.objects.filter(product_category=chosen_category)

    # Отправляем данные на фронт
    context = {
        'category': chosen_category,
        'products': current_products
    }

    return render(request, 'category.html', context)


def product_page(request, pk):
    # Достаем данные из БД
    chosen_product = Product.objects.get(id=pk)
    context = {
        'product': chosen_product
    }

    return render(request, 'product.html', context)