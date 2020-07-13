from django.contrib import admin

from accounts.models import Account, Renewal


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'surname', 'phone', 'registered_on']


@admin.register(Renewal)
class RenewalAdmin(admin.ModelAdmin):
    list_display = ['account', 'payment_date']