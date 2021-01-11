from django.contrib import admin
from .models import PostContent
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'remarks', 'pub_date')

admin.site.register(PostContent, PostAdmin)
