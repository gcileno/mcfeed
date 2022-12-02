from urllib import request
from django.shortcuts import render
from django.db import models
from core.models import Vendedor, Metas, Filial
from django.db.models import aggregates
from .services import func,detalhado

def home(request):
    #o return render não precisa especificar o caminho
    return render(request,'home.html')

#def teste(request):
#    return render(request, 'teste.html')

def ranking(request):
    prata = Vendedor.objects.all().order_by('-prod_contr').values()
    ouro = Vendedor.objects.all().order_by('-prod_pos').values()
    prod = Vendedor.objects.all().order_by('-prod_ap').values()
   
    return render(request, 'ranking.html',{'prata': prata, 'ouro':ouro, 'prod':prod})

def comissao(request):

    vendedor = Vendedor.objects.get(id=1)
    aReceber_c= vendedor.prod_contr * (func.margem_pg(func.atin(vendedor.prod_contr, vendedor.metas.contr)))
    atingimento_c = func.atin(vendedor.prod_contr, vendedor.metas.contr)
    margemR= func.margem_pg(atingimento_c)

    ating_p= func.atin(vendedor.prod_pos,vendedor.metas.pos)
    margem_p=func.margem_pg(ating_p)
    aRec_p = vendedor.prod_pos * margem_p

    context= {
        'vendedor':vendedor,
        'aReceber_c':aReceber_c,
        'atingimento_c':atingimento_c,
        'margemR': margemR,
        'ating_p': ating_p,
        'margem_p':margem_p,
        'aRec_p':aRec_p,
        }

    return render(request, 'valor_com.html',context=context)

def detal(request):

    vendedores = Vendedor.objects.filter(filial__id=1).all()

    #aqui eu vou receber o id e aplicar os dois filtros

    context={
        'vendedores': vendedores,
    }

    return render(request,'detalhado.html', context)

def mcfeed(request):
    return render(request,'mcfeed.html')

def campanha(request):
    return render(request, 'campanha.html')

def prevcom(request):
    a=['controle', 'pos', 'aparelho', 'serviço','pre recarga', 'seguro','aparelho fidel']


    return render(request,'prevcom.html' ,{'as': a})

