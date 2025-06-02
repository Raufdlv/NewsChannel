from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


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

    # Отправляем данные на фронт
    context = {
        'product': chosen_product
    }

    return render(request, 'product.html', context)


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm()}
        return render(request, self.template_name, context)

    # Этап 2 - отправка формы
    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            # Достали данные, которые ввел пользователь
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            # Создаем нового пользователя в БД
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Аутентифицируем пользователя
            login(request, user)

            # Переводим пользователя на главную страницу
            return redirect('/')



# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')