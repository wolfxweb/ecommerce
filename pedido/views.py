from django.shortcuts import render

from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class FecharPedido(View):
     def get(self, *args, **kwargs):
        return HttpResponse('Fechar pedido')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('login')


class Detalhes(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhes')
