from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(title):
    menu = Menu.objects.get(menu_title=title)
    return {'menu': menu}
