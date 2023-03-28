from django.contrib import admin
from .models import Developer
from .models import Category
from .models import Post

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

    ordering = ('friendly_name',)

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publish_date',
    )

    ordering = ('publish_date',)
    
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)