from urllib import request
from django.shortcuts import render, redirect
from django.db import models
from core.models import Vendedor, Metas, Filial
from django.db.models import aggregates
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import RedirectView
from .services import func,detalhado



#Views para gestão de logins

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Usuário ou senha inválidos.')        
    return redirect('/')
    
def logout_user(request):
    logout(request)
    return redirect('/')


#consultas ao banco de dados para alimentar as views e retornar os valores

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def ranking(request):
    prata = Vendedor.objects.all().order_by('-prod_contr').values()
    ouro = Vendedor.objects.all().order_by('-prod_pos').values()
    prod = Vendedor.objects.all().order_by('-prod_ap').values()
   
    return render(request, 'ranking.html',{'prata': prata, 'ouro':ouro, 'prod':prod})

@login_required(login_url='login')
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

@login_required(login_url='login')
def detal(request):

    vendedores = Vendedor.objects.filter(filial__id=1).all()

    #aqui eu vou receber o id e aplicar os dois filtros

    context={
        'vendedores': vendedores,
    }

    return render(request,'detalhado.html', context)

@login_required(login_url='login')
def mcfeed(request):
    return render(request,'mcfeed.html')

@login_required(login_url='login')
def campanha(request):
    return render(request, 'campanha.html')

@login_required(login_url='login')
def prevcom(request):
    a=['controle', 'pos', 'aparelho', 'serviço','pre recarga', 'seguro','aparelho fidel']


    return render(request,'prevcom.html' ,{'as': a})

