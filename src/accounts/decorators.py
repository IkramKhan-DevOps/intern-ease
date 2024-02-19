from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def customer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/cross-auth/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer and not u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/cross-auth/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_company and not u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def identification_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/cross-auth/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_completed,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator