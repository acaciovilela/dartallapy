from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Person, Customer, Supplier, Address, Contact

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1
    fields = (('name', 'number'),)

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1
    fields = (('email', 'site'),('phone', 'cell'))

class PersonAdmin(admin.ModelAdmin):
    model = Person
    inlines = [AddressInline, ContactInline]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
    pass

class SupplierAdmin(admin.ModelAdmin):
    pass

# inlines = [PersonInline]
# list_display = ('name', 'document')
# list_filter = ['PersonInline.register_date']
# list_per_page = 10
# search_fields = ['name']

admin.site.register(Customer, PersonAdmin)
admin.site.register(Supplier, PersonAdmin)
