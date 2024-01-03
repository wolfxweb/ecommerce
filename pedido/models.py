from django.db import models

from django.contrib.auth.models import User



class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField( blank=True, null=True)
    STATUS_CHOICES = [
        ("A", "Aprovado"),
        ("C", "Criado"),
        ("R", "Reprovado"),
        ("P", "Pendente"),
        ("E", "Envido"),
        ("F", "Finalizado"),
    ]

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='C',  # Set the default status as 'Criado'
    )
    def __str__(self) -> str:
        return f'Pedido N. {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveBigIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveBigIntegerField()
    preco = models.FloatField()
    quantidade = models.PositiveBigIntegerField()
    imagen = models.CharField(max_length = 20000)
    preco_promocional = models.FloatField(default=0, blank=True, null=True)
    imagem = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self) -> str:
        return f"Item do {self.pedido}"
    class Meta:
        verbose_name ='Item do pedido'
        verbose_name_plural= 'Itens do pedido'