from django.contrib import admin

# Register your models here.
from blog.models import PostModel

admin.site.register(PostModel)

