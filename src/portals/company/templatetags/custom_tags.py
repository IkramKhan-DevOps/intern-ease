from django import template

register = template.Library()


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url


@register.filter
def image_or_placeholder(image, extras='100'):
    if image:
        return image.url
    return f"https://placeholder.co/{extras}"


@register.filter
def get_review_stars(value):
    html = ''
    value = int(value)
    active_stars = value
    inactive_stars = 5 - value

    for _ in range(active_stars):
        html += '<i class="fa fa-star text-warning"></i>'

    for _ in range(inactive_stars):
        html += '<i class="fa fa-star text-secondary"></i>'

    return html


@register.filter
def alert_type_class(value):
    if value in ['cod', 'delivery', 'in_transit', 'bank_account', "MANAGER", "trialing"]:
        return 'primary'
    if value in ['cod', 'delivery', 'in_transit', 'bank_account', "CASHIER", "incomplete", "incomplete_expired"]:
        return 'info'
    elif value in ['completed', 'success', 'approved', 'paid', 'card', "OWNER", "active"]:
        return 'success'
    elif value in ['pending', "STAFF", "ADMIN", "past_due", "pause"]:
        return 'warning'
    elif value in ['online', 'cancel', 'cancelled', 'unpaid', 'failed', "ROOT"]:
        return 'danger'
    else:
        return 'secondary'


@register.filter
def check_null(value):
    if value:
        return value
    return ""


@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    return qty * unit_price


@register.filter(name='cool_num', is_safe=False)
def cool_number(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M, 1.2B, 5.7T...)
    :param value: number
    :param num_decimals: Number of decimal digits
    """

    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('0').rstrip('.') + 'K'
    elif int_value < 1000000000:
        return formatted_number.format(int_value/1000000.0).rstrip('0').rstrip('.') + 'M'
    elif int_value < 1000000000000:
        return formatted_number.format(int_value/1000000000.0).rstrip('0').rstrip('.') + 'B'
    else:
        return formatted_number.format(int_value/1000000000000.0).rstrip('0').rstrip('.') + 'T'