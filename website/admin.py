from django.contrib import admin
from website.models import Connect
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('name','email','create_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Connect,ContactAdmin)