from django.urls import path
from kev_estore.views import UpdateProduct
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [  # Leave as empty string for base url
    path('', views.home, name='home'),
    path('golfgear/', views.golfgear, name='golfgear'),
    path('robots.txt',
         TemplateView.as_view(template_name='Kev_Project5/robots.txt',
         content_type='text/plain')),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:pk>/', UpdateProduct.as_view(),
         name='update_product'),
    path('delete_product/<int:pk>/', views.DeleteProduct.as_view(),
         name='delete_product'),
    path('product_management/', views.product_management,
         name='product_management'),
    path('update_golfgear/', views.update_golfgear,
         name='update_golfgear'),
    path('delete_golfgear/', views.delete_golfgear,
         name='delete_golfgear'),
    ]

handler404 = 'kev_estore.views.page_not_found'