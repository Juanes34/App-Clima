from django.shortcuts import render
from .models import Page

# Create your views here.
def paginas(request,slug):
    page = Page.objects.get(slug=slug)
    return render(request,'paginas.html',{
        'page':page
    })