from django import template

register = template.Library()

@register.inclusion_tag('username_info.html')
def user_info(user):
    return {
        'user':user.username
    } if user.is_authenticated else {'user':'Anonymous'}