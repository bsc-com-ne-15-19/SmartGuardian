from django.apps import AppConfig


class ApigatewayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APIGateway'
    
    def ready(self):
        import APIGateway.signals