from ast import arg
from audioop import reverse
from contextlib import nullcontext
from enum import unique
from django.db import models

class Filial(models.Model):
    nome = models.CharField(max_length=4,null=True)
    
    def __str__(self):
        return f'{self.nome}'

class Metas (models.Model):
    
    contr = models.IntegerField(null = True)
    pos = models.IntegerField(null = True)
    pre_rec = models.IntegerField(null = True)
    servico = models.FloatField(null = True)        
    aparelho = models.FloatField(null = True)
    acessorio = models.IntegerField(null = True)
    seguro = models.IntegerField(null= True)


class Vendedor (models.Model):
    nome = models.CharField(max_length = 90)
    matricula = models.CharField(max_length = 9, unique= True, null = True)
    prod_contr = models.IntegerField(null = True)
    prod_pos = models.IntegerField(null = True)
    prod_ap= models.FloatField(null = True) 
    metas = models.ForeignKey('Metas',on_delete=models.SET_NULL,null=True)
    filial=models.ForeignKey('Filial',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.matricula} {self.nome}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('vendedor-detail', args=[str(self.id)])


        



    

    


