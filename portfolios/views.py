# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import DadosPessoais

# Create your views here.


def portfolio_exibir(request):

    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}
    return render(request, 'portfolios/portfolio_exibir.html', context)
