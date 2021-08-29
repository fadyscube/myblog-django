from django.contrib import admin

from .models import Post

from django.contrib.auth.models import Group

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)

admin.site.site_header = 'Myblog Administration'

admin.site.site_title = 'Myblog'
