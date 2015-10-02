from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        
admin.site.register(Post, PostAdmin)