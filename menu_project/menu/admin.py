from django.contrib import admin

from .models import Menu, MenuItem, SubItem, SubSubItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    show_change_link = True


class SubSubItemInline(admin.StackedInline):
    model = SubSubItem
    show_change_link = True


class SubItemInline(admin.StackedInline):
    model = SubItem
    show_change_link = True


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline, ]
    list_display = ('menu_title',)
    search_fields = ('menu_title',)


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [SubItemInline, ]
    list_display = ('item_name', 'link', 'seq_num')
    list_filter = ('menu_obj',)
    search_fields = ('menu_obj', 'item_name')


class SubItemAdmin(admin.ModelAdmin):
    inlines = [SubSubItemInline, ]
    list_display = ('subitem_name', 'link', 'seq_num')
    list_filter = ('menu',)
    search_fields = ('subitem_name', 'submenu')


class SubSubItemAdmin(admin.ModelAdmin):
    list_display = ('subsubitem_name', 'link', 'seq_num')
    list_filter = ('submenu',)
    search_fields = ('subsubitem_name', 'submenu')


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(SubItem, SubItemAdmin)
admin.site.register(SubSubItem, SubSubItemAdmin)
