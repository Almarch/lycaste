from django.shortcuts import render
from main.models import Taxon, Genotype, Cross

# Create your views here.

def redirect(request):
    return render(request,'redirect.html')

def welcome(request,lang):
    return render(
        request,
        'welcome.html', {
            'lang': lang,
        }
    )

def taxon_list(request, lang):
    taxons = Taxon.objects.all()
    return render(
        request,
        'taxon_list.html', {
            'lang': lang,
            'taxons': taxons,
        }
    )

def taxon_detail(request, lang, name):
    taxon = Taxon.objects.get(name=name)
    return render(
        request,
        'taxon_detail.html', {
            'lang': lang,
            'taxon': taxon,
        }
    )