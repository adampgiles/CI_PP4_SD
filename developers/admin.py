from django.contrib import admin
from .models import Developer
from .models import Category

# Register your models here.

class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'profile_name',
        'category',
        'price',
        'count_sold',
        'image',
    )

    ordering = ('profile_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Category, CategoryAdmin)