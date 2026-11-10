from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "status",
        "create_at",
    )

    list_filter = ("status")
    search_fields = ("id","product")
