from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PizzaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.pizza"
    verbose_name = _("Pizza")
