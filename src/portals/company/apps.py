from django.apps.config import AppConfig


class CompanyAppConfig(AppConfig):
    name = 'src.portals.company'
    verbose_name = 'Company'

    def ready(self):
        import src.portals.company.signals
