from django.core.management.base import BaseCommand

from menu.models import Menu, MenuItem, SubItem, SubSubItem


class Command(BaseCommand):
    help = u'Создание образца меню'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help=u'Наименование меню.')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        try:
            menu = Menu.objects.get(menu_title=title)
        except Menu.DoesNotExist:
            menu = None
        if menu:
            self.stdout.write(self.style.WARNING(
                'Меню с таким наименованием уже существует.'
            ))
        else:
            menu = Menu.objects.create(menu_title=title)
            MenuItem.objects.bulk_create([
                MenuItem(item_name='Products',
                         link='#',
                         seq_num=1,
                         menu_obj=menu),
                MenuItem(item_name='Cases',
                         link='#',
                         seq_num=2,
                         menu_obj=menu),
                MenuItem(item_name='Company',
                         link='#',
                         seq_num=3,
                         menu_obj=menu),
                MenuItem(item_name='Blog',
                         link='#',
                         seq_num=4,
                         menu_obj=menu),
            ])
            products_item = MenuItem.objects.get(pk=1)
            cases_item = MenuItem.objects.get(pk=2)
            SubItem.objects.bulk_create([
                SubItem(subitem_name='Subproduct1',
                        link='#',
                        seq_num=1,
                        menu=products_item),
                SubItem(subitem_name='Subproduct2',
                        link='#',
                        seq_num=2,
                        menu=products_item),
                SubItem(subitem_name='Subproduct3',
                        link='#',
                        seq_num=3,
                        menu=products_item),
                SubItem(subitem_name='Subcase1',
                        link='#',
                        seq_num=1,
                        menu=cases_item),
                SubItem(subitem_name='Subcase2',
                        link='#',
                        seq_num=2,
                        menu=cases_item)
            ])
            subproduct_1 = SubItem.objects.get(pk=1)
            subcase_1 = SubItem.objects.get(pk=4)
            SubSubItem.objects.bulk_create([
                SubSubItem(subsubitem_name='Subsubproduct1',
                           link='#',
                           seq_num=1,
                           submenu=subproduct_1),
                SubSubItem(subsubitem_name='Subsubproduct2',
                           link='#',
                           seq_num=2,
                           submenu=subproduct_1),
                SubSubItem(subsubitem_name='Subsubcase1',
                           link='#',
                           seq_num=1,
                           submenu=subcase_1),
                SubSubItem(subsubitem_name='Subsubcase2',
                           link='#',
                           seq_num=2,
                           submenu=subcase_1)
            ])
            self.stdout.write(self.style.SUCCESS(
                f'Меню с наименованием "{title}" успешно создано.'
            ))
