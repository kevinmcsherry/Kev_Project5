from django.shortcuts import render
from .models import *


def home(request):
	context = {}
	return render(request, 'kev_estore/home_page.html', context)

def clothes(request):
	clothings = Clothing.objects.all()
	context = {'clothings':clothings}
	return render(request, 'kev_estore/clothes.html', context)

def accessories(request):
	accessories = Accessories.objects.all()
	context = {'accessories':accessories}
	return render(request, 'kev_estore/accessories.html', context)

def clubs(request):
	clubs = Clubs.objects.all()
	context = {'clubs':clubs}
	return render(request, 'kev_estore/clubs.html', context)

def basket(request):
	context = {}
	return render(request, 'kev_estore/basket.html', context)

def checkout(request):
	context = {}
	return render(request, 'kev_estore/checkout.html', context)
