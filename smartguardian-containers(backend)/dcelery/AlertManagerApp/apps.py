from django.apps import AppConfig


class AlertmanagerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AlertManagerApp'
    
    def ready(self):
        import AlertManagerApp.signals