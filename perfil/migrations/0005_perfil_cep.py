# Generated by Django 5.0 on 2024-01-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil", "0004_alter_perfil_complemento"),
    ]

    operations = [
        migrations.AddField(
            model_name="perfil",
            name="cep",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
