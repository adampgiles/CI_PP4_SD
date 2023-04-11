from django.contrib import admin
from .models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

    ordering = ('user',)

admin.site.register(UserAccount, UserAccountAdmin)
