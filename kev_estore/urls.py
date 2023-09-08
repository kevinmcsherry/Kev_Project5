from django.urls import path
from .views import CreateAccount
from .views import Login
from .views import page_not_found
from .views import UpdateProduct, DeleteProduct, add_product, delete_golfgear
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView


from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('create_account/', CreateAccount.as_view(), name='create_account'),
	path('', views.home, name="home"),
	path('checkout/', views.checkout, name="checkout"),
	path('golfgear/', views.golfgear, name="golfgear"),
	path('purchase_complete/', views.purchase_complete, name="purchase_complete"),
	path('basket/', views.basket, name="basket"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path("robots.txt",TemplateView.as_view(template_name="Kev_Project5/robots.txt", content_type="text/plain")),
	path('newsletter/', views.newsletter, name='newsletter'),
    path('validate/', views.validate_email, name='validate_email'),
	path('add_product/', views.add_product, name='add_product'),
	path('update_product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
	path('delete_product/<int:pk>/', views.DeleteProduct.as_view(), name='delete_product'),
	path('product_management/', views.product_management, name='product_management'),
	path('update_golfgear/', views.update_golfgear, name='update_golfgear'),
	path('delete_golfgear/', views.delete_golfgear, name='delete_golfgear'),

]

handler404 = "kev_estore.views.page_not_found"
