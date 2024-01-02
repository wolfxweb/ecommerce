from django.db import models
from PIL import Image
import os
from django.conf import settings 
from django.utils.text import slugify
from datetime import datetime
from utils import utils

class Produto(models.Model):
    
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField()
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to="produto_imagem/%Y/%M", blank=True, null=True)
    slug = models.SlugField(unique=True , blank = True, null=True)
    preco_marketing = models.FloatField(verbose_name ='Perço')
    preco_marketing_promocional = models.FloatField(default=0 , verbose_name='Preço Promocional')
    tipo = models.CharField(
        default="V", max_length=1, choices=(("V", "Variação"), ("S", "Simples"))
    )
    status = models.CharField(
        default="A", max_length=1, choices=(("A", "Ativo"), ("I", "Inativo"))
    )

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description ='Preço promocional'
      
    @staticmethod
    def resize_imagem(img , new_width = 800):
      img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
      img_pill = Image.open(img_full_path)
      original_width, original_height= img_pill.size
      
      if original_width <= new_width:
          img_pill.close()
          return 
      
      new_height = round((new_width* original_height)/original_width)
      new_img = img_pill.resize((new_width,new_height), Image.LANCZOS)
      new_img.save(
          img_full_path,
          optimize= True,
          quality=50
      )
      
      
      print(new_height)
       
       
    def save(self, *args, **kwargs):
        current_datetime = datetime.now()

        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

        if not self.slug:
            slug = f'{slugify(self.nome)}-{formatted_datetime}'
            self.slug = slug
            
        super().save(*args, **kwargs)

        max_imagem_size = 200

        if self.imagem:
            self.resize_imagem(self.imagem, max_imagem_size)

    def __str__(self):
        return self.nome

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete= models.CASCADE)
    nome = models.CharField(max_length=50)
    preco =models.FloatField()
    preco_promocional = models.FloatField(default =0)
    estoque = models.PositiveBigIntegerField(default = 1)
    
    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name= 'Variação'
        verbose_name_plural = "Variações"