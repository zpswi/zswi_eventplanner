from django.apps import AppConfig as DjangoConfig


class AppConfig(DjangoConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
