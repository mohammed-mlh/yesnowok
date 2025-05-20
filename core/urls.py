from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category>/', views.category_products, name='category_products'),
    path('<str:category>/<int:product_id>/', views.product_detail, name='product_detail'),
]
