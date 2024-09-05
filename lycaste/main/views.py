from django.shortcuts import render

# Create your views here.

def redirect(request):
    return render(request,'redirect.html')

def fr(request):
    return render(request,'fr.html')