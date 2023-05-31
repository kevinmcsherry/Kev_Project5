from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="shop"),
	path('cart/', views.cart, name="basket"),
	path('checkout/', views.checkout, name="checkout"),

]