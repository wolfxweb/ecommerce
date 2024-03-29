from django.db import models

from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Usuário')
    data_nacimento = models.DateField( blank=True, null=True)
    cpf = models.CharField(max_length =11, blank=True, null=True)
    endereco =  models.CharField(max_length =100)
    numero = models.CharField(max_length =10)
    complemento  = models.CharField(max_length = 200, blank=True, null=True)
    bairro = models.CharField(max_length = 100)
    cidade = models.CharField( max_length=100)
    estado = models.CharField(
        default="SP",
        max_length=2, 
        choices=(
           ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
            )
        )
    cep = models.CharField(max_length =20, blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.usuario.first_name}'
    
    def clean(self):
        pass

    class Meta:
        verbose_name= 'Perfil'
        verbose_name_plural = "Prefis"