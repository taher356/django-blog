from django.contrib import admin

# Register your models here.
from blog.models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_view','status','publish_date')
    list_filter = ('status',)
    search_fields = ['title','content']
admin.site.register(PostModel,PostModelAdmin)
