from django.shortcuts import render
from main.models import Taxon
from main.forms import TaxonForm

def redirect(request):
    return render(request,'redirect.html')

def welcome(request,lang):
    return render(
        request,
        'fr_welcome.html', {
            'lang': lang,
        }
    )

def taxon_list(request, lang):
    taxons = Taxon.objects.all()
    return render(
        request,
        'fr_taxon_list.html', {
            'lang': lang,
            'taxons': taxons,
        }
    )

def taxon_detail(request, lang, name):
    taxon = Taxon.objects.get(name=name)
    return render(
        request,
        'fr_taxon_detail.html', {
            'lang': lang,
            'taxon': taxon,
        }
    )

def taxon_create(request, lang):
    if request.method == 'POST':
        form = TaxonForm(request.POST)
        if form.is_valid():
            taxon = form.save()
            return redirect('taxon-detail', lang, taxon.name)

    else:
        form = TaxonForm()

    return render(
        request,
        'taxon_create.html',
        {
            'title': 'New taxon',
            'form': form,
        }
    )

def taxon_update(request, lang, name):
    taxon = Taxon.objects.get(name=name)

    if request.method == 'POST':
        form = TaxonForm(request.POST, instance=taxon)
        if form.is_valid():
            form.save()
            return redirect('taxon-detail', lang, taxon.name)
    else:
        form = TaxonForm(instance=taxon)

    return render(
        request,
        'taxon_create.html',
        {
            'title': 'Update Taxon',
            'form': form,
        }
    )
