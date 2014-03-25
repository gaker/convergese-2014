"""
Post admin
"""
from django.contrib import admin
from company.apps.blog.models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Customize the post admin page.
    """
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)
