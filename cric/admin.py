from django.contrib import admin
from django.test import tag

from .models import User, comments, singer, songs, Tags


admin.site.register(User)
admin.site.register(comments)
admin.site.register(singer)
admin.site.register(songs)
admin.site.register(Tags)



# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['id','name','email','password']

# @admin.register(singer)
# class SingerAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'gender', 'age','createdAt','updatedAt']


# @admin.register(songs)
# class SongsAdmin(admin.ModelAdmin):
#     list_display=['id','title','duration','sungby','tags','createdAt','updatedAt']

# @admin.register(Tags)
# class TagAdmin(admin.ModelAdmin):
#     list_display=['id','title']

# @admin.register(comments)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['id','user','comment','song','createdAt','updatedAt']

