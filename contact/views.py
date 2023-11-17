from django.shortcuts import render


# Create your views here.


def newsletter(request):
    '''
    Link to Newsletter signup
    form
    '''
    return render(request, 'newsletter.html')
