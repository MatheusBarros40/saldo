from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transacao, atualizar_saldo

# Sinal para atualizar o saldo após salvar ou atualizar uma transação
@receiver(post_save, sender=Transacao)
def transacao_post_save(sender, instance, **kwargs):
    atualizar_saldo()

# Sinal para atualizar o saldo após excluir uma transação
@receiver(post_delete, sender=Transacao)
def transacao_post_delete(sender, instance, **kwargs):
    atualizar_saldo()
