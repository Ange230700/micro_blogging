# accounts\service\apps.py

"""Django app configuration for the service app."""

from django.apps import AppConfig


class ServiceConfig(AppConfig):

    """Configuration class for the service application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "service"
