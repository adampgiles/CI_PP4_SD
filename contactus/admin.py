from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    ''' Admin display for ContactUs model '''
    list_display = (
        'user',
        'sent_date',
        'subject',
    )

    ordering = ('sent_date',)

admin.site.register(ContactUs, ContactUsAdmin)