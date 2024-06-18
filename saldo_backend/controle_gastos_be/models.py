from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    DESPESA = 'despesa'
    RECEITA = 'receita'
    TIPO_CHOICES = [
        (DESPESA, 'Despesa'),
        (RECEITA, 'Receita'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, related_name='transacoes', on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.valor}"

class Saldo(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Saldo: {self.valor}"

def atualizar_saldo():
    saldo, _ = Saldo.objects.get_or_create(id=1)  # Cria ou obtém o único objeto Saldo
    despesas = Transacao.objects.filter(tipo=Transacao.DESPESA).aggregate(Sum('valor'))['valor__sum'] or 0
    receitas = Transacao.objects.filter(tipo=Transacao.RECEITA).aggregate(Sum('valor'))['valor__sum'] or 0
    saldo.valor = receitas - despesas
    saldo.save()

# Sinal para atualizar o saldo após salvar ou atualizar uma transação
@receiver(post_save, sender=Transacao)
def transacao_post_save(sender, instance, **kwargs):
    atualizar_saldo()

# Sinal para atualizar o saldo após excluir uma transação
@receiver(post_delete, sender=Transacao)
def transacao_post_delete(sender, instance, **kwargs):
    atualizar_saldo()
