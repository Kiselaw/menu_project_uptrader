from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def show_results(title):
    menu = Menu.objects.get(menu_title=title)
    print(menu.items)
    # for item in menu_items:
    #     a = item.subitems.all()
    #     print(a)
    # print(menu_items)
    return {'menu': menu}
