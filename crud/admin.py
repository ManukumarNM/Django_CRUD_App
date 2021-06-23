from django.contrib import admin
from . models import Students

admin.site.register(Students)

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('fname', 'email', 'contact_number', 'subject', 'message')
# admin.site.register(Contact, ContactAdmin)

