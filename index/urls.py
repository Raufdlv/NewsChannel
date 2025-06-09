from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('product/<int:pk>', views.product_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('favorite', views.favorite),
    path('to-favorite/<int:pk>', views.add_to_favorite),
    path('del-from-favorite/<int:pk>', views.del_from_favorite),
    path('favorite', views.favorite),
]