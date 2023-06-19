from django.shortcuts import render


def clothes(request):
	context = {}
	return render(request, 'kev_estore/clothes.html', context)

def accessories(request):
	context = {}
	return render(request, 'kev_estore/accessories.html', context)

def clubs(request):
	context = {}
	return render(request, 'kev_estore/clubs.html', context)



def basket(request):
	context = {}
	return render(request, 'kev_estore/basket.html', context)

def checkout(request):
	context = {}
	return render(request, 'kev_estore/checkout.html', context)
