from django.urls import path
from .views import CreateAccount
from .views import Login
from .views import page_not_found
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
	path('basket/', views.basket, name="basket"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path("robots.txt",TemplateView.as_view(template_name="Kev_Project5/robots.txt", content_type="text/plain")),
	path('newsletter/', views.newsletter, name='newsletter'),
    path('validate/', views.validate_email, name='validate_email'),
	path('add_product/', views.add_product, name='add_product'),
	path('product_management/', views.product_management, name='product_management'),
]

handler404 = "kev_estore.views.page_not_found"
