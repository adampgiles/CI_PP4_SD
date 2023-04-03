from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',
                       'original_cart','stripe_pid')

    fields = ('order_number', 'date', 'username',
              'email', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'username',
                    'total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)