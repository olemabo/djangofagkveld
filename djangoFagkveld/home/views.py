from django.shortcuts import render

from .models import StandardPage

# Create your views here.

def index(request):
    """ View function for home page """

    home_page = StandardPage.objects.all().first()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    print(home_page)

    context = {
        'heading': home_page.heading,
        'ingress': home_page.ingress, 
        'num_visits': num_visits, 
    }

    return render(request, 'index.html', context=context)