from django.db import models
from django.utils import timezone


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class ContaPagar(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    paga = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - R${self.valor}"


class Venda(models.Model):
    METODOS_PAGAMENTO = [
        ('Credito', 'Crédito'),
        ('Debito', 'Débito'),
        ('PIX', 'PIX'),
        ('Dinheiro', 'Dinheiro'),
        ('Voucher', 'Voucher'),
    ]

    cliente = models.CharField(max_length=100, default='Usuario')
    data = models.DateField(default=timezone.now)
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO, default='Credito')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venda #{self.id} - {self.cliente}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def preco_total(self):
        return self.quantidade * self.preco_unitario