# Generated by Django 5.0 on 2024-01-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pedido", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="qtd_total",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
