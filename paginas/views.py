from django.shortcuts import render

class IndexView(TemplateView) :
    template_name = 'paginas/index.html'

class SobreView(TemplateView) :
    template_name = 'paginas/sobre.html'


# Create your views here.
