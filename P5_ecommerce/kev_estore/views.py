from django.shortcuts import render


def store(request):
	context = {}
	return render(request, 'kev_estore/shop.html', context)

def cart(request):
	context = {}
	return render(request, 'kev_estore/basket.html', context)

def checkout(request):
	context = {}
	return render(request, 'kev_estore/checkout.html', context)
