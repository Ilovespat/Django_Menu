from django import template
from django.template import RequestContext

from ..models import MenuBar

register = template.Library()


@register.inclusion_tag('Menu/menu_pattern.html', takes_context=True)
def draw_menu(context, menu_name):
    req = context['request']
    url_path = req.path.replace("/", "")
    menu_queryset = (MenuBar.objects
                     .filter(category__name=menu_name)
                     .select_related('parent'))
    children = getchildren(menu_queryset)
    return {'menu': menu_queryset, 'children': children, 'url_path': url_path}


def getchildren(query):
    ListChild = []
    for item in query:
        ListChild.append(str(item.parent))
    return ListChild
