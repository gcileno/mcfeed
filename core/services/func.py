from django.db import models
from core.models import Vendedor
from django.db.models import aggregates

def qual_pos(pos,qual):
    pos=pos.copy()
    for k,v in pos.items():
        pos[k]= v* qual['POS']
    return pos

def qual_cont(contr,qual):
    contr=contr.copy()
    for k,v in contr.items():
        contr[k]= v* qual['CONTROLE']
    return contr

def atin(prod_cont,meta):
    a = (prod_cont/meta)*100
    return a

#gatilhos de comissão
def gat_ps(contr,pos,a,b,c,d):

    if atin(a,b)<80 or atin(c,d)<80:
        for k,v in contr.items():
            contr[k]=v*0.0952380952380952
        for k,v in pos.items():
            pos[k]=v*0.0952380952380952
        return contr, pos



# margem de pagamento dos serviços esta recebendo dois dicionarios ainda não criados
def margem_pg(a):

    if a >= 90.0 and a<100.0:
           return 11.50*0.7142857142857143
   
    elif a >= 80.0 and a < 90.0:    
        return 11.50*0.333522
    
    elif a <= 70 and a < 80.0:
            return 11.50*0.0952380952380952                    

    else:
        return 11.50*1

    
    
