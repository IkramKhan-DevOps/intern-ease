from src.website.utils import get_or_create_application


def application(request):
    return {'app': get_or_create_application()}
