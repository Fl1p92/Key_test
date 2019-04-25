from django import template
from django.urls import reverse


register = template.Library()


@register.simple_tag
def get_admin_url(obj):
    admin_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=(obj.pk,))
    return admin_url
