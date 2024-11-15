from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book"
    varbose_name='读书'
