from django.apps import AppConfig

class ControleGastosBeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'controle_gastos_be'

    def ready(self):
        import controle_gastos_be.signals  # Importa os sinais para conectar
