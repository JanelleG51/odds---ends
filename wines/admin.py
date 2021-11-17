from django.contrib import admin
from .models import Wine, Case, Category

# Register your models here.


class WineAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'country',
        'region',
        'winery',
        'rating',
        'price',
        'year',
        'image',

    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',

    )


admin.site.register(Wine, WineAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Category, CategoryAdmin)
