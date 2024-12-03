from django.contrib import admin
from.models import *
admin.site.index_title="MARTIN Programmer"
admin.site.site_header="MARTIN Programmer Pro"

# admin.site.register(Property)
# admin.site.register(Tenant)
# admin.site.register(Lease)
# admin.site.register(Unit)
@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display=("id","start_date","end_date")
    ordering=['id']
    search_fields=('id',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=("id","name","address","description")
    ordering=['id']
    search_fields=('id',)

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display=("id","name","email","phone_number")
    ordering=['id']
    search_fields=('id',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display=("id","bedrooms","is_available","property","unit_number","rent")
    ordering=['id']
    search_fields=('id',)

