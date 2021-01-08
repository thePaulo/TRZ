from django.apps import AppConfig


class SurvivorsConfig(AppConfig):
    name = 'survivors'
    def ready(self):
        import survivors.signals
