from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from cash4you.models import Produto, Servico, ContaPagar
from cash4you.forms import ProdutoForm, ServicoForm, ContaPagarForm

def home(request):
    # Lógica de dashboard / relatórios resumidos
    produtos = Produto.objects.all()
    servicos = Servico.objects.all()
    contas = ContaPagar.objects.all().order_by('vencimento')[:5]
    
    context = {
        'total_produtos': sum(p.preco_venda * p.quantidade for p in produtos),
        'total_servicos': sum(s.preco for s in servicos),
        'contas': contas,
    }
    return render(request, 'home.html', context)

def adicionar(request):
    tipo = request.GET.get('tipo', 'produto')
    
    if request.method == 'POST':
        if tipo == 'produto':
            form = ProdutoForm(request.POST)
        elif tipo == 'servico':
            form = ServicoForm(request.POST)
        else:
            form = ContaPagarForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect(f'/adicionar/?tipo={tipo}')
    else:
        form_prod = ProdutoForm()
        form_serv = ServicoForm()
        form_conta = ContaPagarForm()

    context = {
        'tipo_atual': tipo,
        'form_prod': form_prod,
        'form_serv': form_serv,
        'form_conta': form_conta,
        'produtos': Produto.objects.all(),
        'servicos': Servico.objects.all(),
        'contas': ContaPagar.objects.all(),
    }
    return render(request, 'adicionar.html', context)

def visualizar(request):
    tipo = request.GET.get('tipo', 'produto')
    context = {
        'tipo': tipo,
        'produtos': Produto.objects.all(),
        'servicos': Servico.objects.all(),
        'contas': ContaPagar.objects.all(),
    }
    return render(request, 'visualizar.html', context)

def caixa(request):
    context = {
        'produtos': Produto.objects.all(),
        'servicos': Servico.objects.all(),
    }
    return render(request, 'caixa.html', context)

def relatorios(request):
    return render(request, 'relatorios.html')

def excluir_item(request, tipo, pk):
    models_map = {'produto': Produto, 'servico': Servico, 'conta': ContaPagar}
    model = models_map.get(tipo)
    if model:
        item = get_object_or_404(model, pk=pk)
        item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))
