from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

def home(request):
    gall=Gallery.objects.all()
    return render(request, 'Visa/home.html', {'gall':gall})
