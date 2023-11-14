from django.urls import path
from . import views

urlpatterns = [path('checkout/', views.checkout, name='checkout'),
               path('purchase_complete/', views.purchase_complete,
               name='purchase_complete'), path('basket/', views.basket,
               name='basket'), path('process_order/',
               views.processOrder, name='process_order'),
               path('update_item/', views.updateItem, name='update_item'
               )]