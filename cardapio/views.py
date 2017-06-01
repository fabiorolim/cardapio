from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cardapio.models import Cardapio
from cardapio.forms import FormularioCardapio
# Create your views here.
@login_required
def listar(request):
    query = request.GET.get('busca')
    if query:
       cardapios = Cardapio.objects.filter(prato_principal__icontains=query)
    else:
        cardapios = Cardapio.objects.all()
    return render(request, 'index.html', {'cardapios': cardapios})


@login_required
def cadastrar(request):
    form = FormularioCardapio(request.POST or None)
    if form.is_valid():
        cardapio = form.save(commit=False)
        cardapio.usuario = get_logado(request)
        cardapio.save()
        return redirect('cardapios:listar')
    return render(request, 'novo_cardapio.html', {'form': form})


@login_required
def exibir(request, cardapio_id):
    cardapio = Cardapio.objects.get(id=cardapio_id)
    return render(request, 'cardapio.html', {'cardapio': cardapio})


@login_required
def editar(request, cardapio_id):
    cardapio = Cardapio.objects.get(id=cardapio_id)
    if request.method == "POST":
        form = FormularioCardapio(request.POST, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('cardapios:listar')
    else:
        form = FormularioCardapio(instance=cardapio)
    return render(request, 'editar_cardapio.html', {'form': form})


@login_required
def deletar(request, cardapio_id):
    cardapio = Cardapio.objects.get(id = cardapio_id)
    if request.method != "POST":
        cardapio.delete()
    return redirect('cardapios:listar')


@login_required
def get_logado(request):
   return request.user