from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'createAt']
    list_filter = ['createAt']
    search_fields = ['id']
    inlines = [CommentInline]
admin.site.register(Post, PostAdmin)