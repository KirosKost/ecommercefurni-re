from django.contrib import admin
from .models import Post


# class PostConfig(admin.ModelAdmin):
#     fields = ('title',
#               'img',
#               'description',
#               )
#     list_display = ('name', 'img', 'description')
#     admin.site.register(Review)
admin.site.register(Post)
