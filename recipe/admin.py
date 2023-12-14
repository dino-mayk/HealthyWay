from django.contrib import admin

from recipe.models import Comment, Recipe


@admin.register(Recipe)
class AdminPosts(admin.ModelAdmin):
    list_display = [
        'title',
    ]

@admin.register(Comment)
class AdminComments(admin.ModelAdmin):
    list_display = [
        'id',
        "show",
    ]
