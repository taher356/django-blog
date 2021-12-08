from django.contrib import admin

# Register your models here.
from blog.models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_view','status','publish_date')
    list_filter = ('status','author')
    search_fields = ['title','content']
    #ordering = ['create_date']
admin.site.register(PostModel,PostModelAdmin)
