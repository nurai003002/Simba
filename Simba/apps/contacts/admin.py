from django.contrib import admin
from apps.contacts.models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'whatsapp', 'inst', 'email', 'address']