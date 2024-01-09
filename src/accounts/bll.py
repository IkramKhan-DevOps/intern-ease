def account_student_create(user):
    """
    CHECK-1: CREATE_STUDENT_PROFILE
    CHECK-2: CREATE_ZOOM_PROFILE

    :param user:
    :return none:
    """
    pass


def account_admin_create(user):
    """
    :param user:
    :return none:
    """
    pass


def account_moderator_create(user):
    """
    :param user:
    :return:
    """


def account_parent_create(user):
    """
    :param user:
    :return:
    """


def account_identification_registration(user, user_type):
    response_message = "Please provide correct user type here."
    response_result = False

    if user_type in ['m', 'a', 's', 'p']:
        if user_type == 'a':
            account_admin_create(user=user)
            response_message = "Your are successfully registered as Admin"
        elif user_type == 's':
            account_student_create(user=user)
            response_message = "Your are successfully registered as customer"
        elif user_type == 'm':
            account_moderator_create(user=user)
            response_message = "Your are successfully registered as Moderator"
        else:
            account_parent_create(user=user)
            response_message = "Your are successfully registered as Parent"
        response_result = True

    return False, response_message
