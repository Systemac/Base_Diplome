from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Diplomes, Personne, Session


# Create your views here.
def index(request):
    template = loader.get_template('Diplome/index.html')
    session = Session.objects.all()
    personne = Personne.objects.all()
    diplomes = Diplomes.objects.all()
    context = {
        'session': session,
        'personne': personne,
        'diplomes': diplomes,
    }

    return HttpResponse(template.render(context, request))
