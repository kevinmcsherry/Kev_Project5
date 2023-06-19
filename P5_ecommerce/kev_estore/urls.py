from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.clothes, name="clothes"),
	path('accessories/', views.accessories, name="accessories"),
	path('clubs/', views.clubs, name="clubs"),
	path('basket/', views.basket, name="basket"),
	path('checkout/', views.checkout, name="checkout"),

]