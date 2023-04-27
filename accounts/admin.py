from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    ''' Admin display for UserAccount model '''
    list_display = (
        'user',
        'is_developer'
    )

    ordering = ('user',)


admin.site.register(UserAccount, UserAccountAdmin)
