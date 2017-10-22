from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TerrenoForm
from .models import Terreno


def terreno_list(request):
    terrenos = Terreno.objects.all()

    context = {
        'terreno_list': terrenos
    }

    return render(request, 'zoneamento_urbano/terreno_list.html', context)


def terreno_new(request):
    title = "Cadastrar Novo Terreno"
    form = TerrenoForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Terreno cadastro com sucesso!')
        return redirect('zoneamento_urbano:terreno_list')

    context = {
        'title': title,
        'form': form
    }

    return render(request,
                  'zoneamento_urbano/terreno_form.html', context)


def terreno_edit(request, pk):
    title = "Editar Novo Terreno"

    obj = get_object_or_404(Terreno, pk=pk)

    form = TerrenoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Terrno Atualizado com sucesso!')
        return redirect('zoneamento_urbano:terreno_list')

    context = {
        'title': title,
        'form': form
    }

    return render(request,
                  'zoneamento_urbano/terreno_form.html', context)
