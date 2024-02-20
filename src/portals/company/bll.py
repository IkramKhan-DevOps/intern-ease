from src.portals.company.models import (
    Company, Job
)
from src.accounts.models import (
    User, City, Category
)


def get_user_company_bll(user):
    company = None
    try:
        company = Company.objects.get(user=user)
    except Company.DoesNotExist:
        company = Company.objects.create(user=user)
    return company


def recommended_jobs_for_candidate(user):
    """
    Return a list of recommended jobs for a candidate
    based on job city and category wrt user city and categories
    """
    recommended_jobs = []
    try:
        user = User.objects.get(pk=user.id)
        city = user.city
        categories = user.categories.all()
        recommended_jobs = Job.objects.filter(city=city, category__in=categories)
    except User.DoesNotExist:
        pass
    return recommended_jobs


def recommended_candidates_for_job(job):
    """
        Return a list of recommended users for a job
        based on job city and category wrt user city and categories
        """
    recommended_candidates = []
    try:
        job = Job.objects.get(pk=job.id)
        city = job.city
        category = job.category
        recommended_candidates = User.objects.filter(city=city, categories__in=[category])
    except Job.DoesNotExist:
        pass
    return recommended_candidates
