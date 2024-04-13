from django.shortcuts import render, redirect

from cadfilmes.form import FormCadFilmes, FormCategoria


# Create your views here.
def cad_filmes(request):
    template_name = 'cadfilmes/cad_filmes.html'
    form = FormCadFilmes(request.POST or None)
    if request.method == 'GET':
        context = {'form' : form}
        return render(request, template_name, context)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, template_name, context)


def cad_Categoria(request):
    template_name = 'cadfilmes/cad_filmes.html'
    form = FormCategoria(request.POST or None)
    if request.method == 'GET': 
        context = {'form' : form}
        return render(request, template_name, context)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, template_name, context)