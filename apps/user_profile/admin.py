from django.contrib import admin

from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth')
    list_display_links = ('id', 'first_name', 'last_name',)
    search_fields = ('id', 'first_name', 'last_name', 'date_of_birth')
