from django.apps import AppConfig


class TobaccoConfig(AppConfig):
    name = 'tobacco'

    def ready(self):
        import tobacco.signals