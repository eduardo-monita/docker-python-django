from django.contrib import admin

from example_app.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'birth_date', 'active','created_at', 'updated_at']
    list_display_links = ['name', 'cpf']
    fields = ['name', 'cpf', 'birth_date', 'active']
    search_fields = ['name', 'cpf']
    list_filter = ['active']
    list_per_page = 12
    ordering = ['name']

# Register your models here.
