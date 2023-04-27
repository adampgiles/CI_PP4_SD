from django.contrib import admin
from .models import Developer, Category, Post


class DeveloperAdmin(admin.ModelAdmin):
    ''' Admin display for Developer model '''
    list_display = (
        'profile_name',
        'category',
        'price',
        'count_sold',
        'image',
    )

    ordering = ('profile_name',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Admin display for Category model '''
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class PostAdmin(admin.ModelAdmin):
    ''' Admin display for Post model '''
    list_display = (
        'title',
        'publish_date',
    )

    ordering = ('publish_date',)


admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
