from django.contrib import admin
from .models import Phone,Info

# Register your models here.
class DescriptionInline(admin.TabularInline):
    model = Phone
    extra = 1
# admin.site.register(Info)
@admin.register(Info)
class PhoneAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]
    list_display = Info.DisplayFields
    search_fields = Info.SearchableFields