from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from . import models

# admin.site.register(models.Сhairman)
admin.site.register(models.Document)
# admin.site.register(models.Employee)
admin.site.register(models.News)
admin.site.register(models.ShortNewsOnMainPage)
admin.site.register(models.NewsPhoto)


# admin.site.register(models.Appeal)


# Отображение в админ панели


@admin.register(models.Сhairman)
class ChairmanAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "e_mail"]


@admin.register(models.Employee)
class EmploeeAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "e_mail"]


@admin.register(models.Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ["name", "e_mail", "filial"]


class FlatPageAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/j/jquery.js',
              '/media/j/admin_enhancements.js')
        css = {'screen': ('/media/c/admin.css',)}


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
