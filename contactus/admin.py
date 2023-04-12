from django.contrib import admin
from .models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sent_date',
        'subject',
    )

    ordering = ('sent_date',)

admin.site.register(ContactUs, ContactUsAdmin)