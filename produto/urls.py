from django.urls import path
from . import views

app_name='produto'
urlpatterns = [
     path('',views.ListaProdutos.as_view(), name='lista' ),
     path('<slug>',views.DetalhesProdutos.as_view(), name='detalhes' ),
     path('adicionaraocarrinho/',views.AdiconarAoCarrinho.as_view(), name='adiciona_ao_carrinho' ),
     path('removercarrinho/',views.RemoverCarrinho.as_view(), name='remover_carrinho' ),
     path('carrinho/',views.CarrinhoProdutos.as_view(), name='carrinho' ),
     path('finalizar/',views.FinalizarCarrinho.as_view(), name='finalizar' ),
]
