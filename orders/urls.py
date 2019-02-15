from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('process_order/', views.process_order, name='process_order')
]
