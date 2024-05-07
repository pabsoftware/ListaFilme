from django.shortcuts import render
from cadfilmes.models import Filmes 

# Create your views here.

def home(request):
    template_name =  'core/home.html'
    #object_list = Filmes.objects.all().order_by('titulo')
    #context = {'object_list': object_list}
    return render(request, template_name)