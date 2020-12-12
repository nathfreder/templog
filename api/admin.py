from django.contrib import admin
from .models import Temperature


class TemperatureAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('id', 'temperature', 'date')
    list_filter = ('date',)


admin.site.register(Temperature, TemperatureAdmin)
