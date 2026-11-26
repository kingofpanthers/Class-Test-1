from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "year", "price", "fuel_type", "is_available")
    list_filter = ("is_available", "fuel_type")
    search_fields = ("name", "brand")


admin.site.site_header = "Motorline Administration"

admin.site.site_title = "Motorline Admin"
admin.site.index_title = "Dealership dashboard"
admin.site.enable_nav_sidebar = False
