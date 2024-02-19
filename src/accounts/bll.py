
def is_account_complete(user):
    if user.city and user.country and user.categories:
        return True

    return False
