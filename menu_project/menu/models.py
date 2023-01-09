from django.db import models


class Menu(models.Model):
    menu_title = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.menu_title


class MenuItem(models.Model):
    item_name = models.CharField(max_length=150)
    link = models.CharField(max_length=255, null=True, blank=False)
    seq_num = models.IntegerField()
    menu_obj = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='items'
    )

    def __str__(self) -> str:
        return self.item_name


class SubItem(models.Model):
    subitem_name = models.CharField(max_length=150)
    link = models.CharField(max_length=255, null=True, blank=False)
    seq_num = models.IntegerField()
    menu = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='subitems'
    )

    def __str__(self) -> str:
        return self.subitem_name


class SubSubItem(models.Model):
    subsubitem_name = models.CharField(max_length=150)
    link = models.CharField(max_length=255, null=True, blank=False)
    seq_num = models.IntegerField()
    submenu = models.ForeignKey(
        SubItem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='subsubitems'
    )

    def __str__(self) -> str:
        return self.subsubitem_name
