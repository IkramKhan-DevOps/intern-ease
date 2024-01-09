from src.portals.company.models import Company


def get_user_company_bll(user):
    company = None
    try:
        company = Company.objects.get(user=user)
    except Company.DoesNotExist:
        company = Company.objects.create(user=user)
    return company
