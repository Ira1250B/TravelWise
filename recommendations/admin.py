from django.contrib import admin

from .models import TravelPackage


@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "travel_type",
        "price",
        "food_score",
        "nature_score",
    )

    list_filter = ("travel_type",)
    search_fields = ("name", "location")
