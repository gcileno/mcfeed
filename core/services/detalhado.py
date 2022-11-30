from django.db import models
from core.models import Vendedor


def meta_dia(prod,meta,dia_res):
    m=(meta-prod)/dia_res
    return m

def tendencia(prod,meta,dia_res,dias_t):
    t=((((prod/dias_t)*dia_res)+prod)/meta)*100
    return t