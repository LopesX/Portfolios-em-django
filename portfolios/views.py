# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def portfolio_exibir(request):
	return render(request, 'portfolios/portfolio_exibir.html', {})