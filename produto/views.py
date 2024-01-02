from django.shortcuts import render

from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name ='produto/lista.html' 
    context_object_name='produtos'
    paginate_by = 10
    
    
class DetalhesProdutos(DetailView):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalhesProdutos')


class AdiconarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdiconarAoCarrinho')


class RemoverCarrinho(View):
   def get(self, *args, **kwargs):
        return HttpResponse('RemoverCarrinho')


class CarrinhoProdutos(View):
      def get(self, *args, **kwargs):
        return HttpResponse('CarrinhoProdutos')

class FinalizarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FinalizarCarrinho')
