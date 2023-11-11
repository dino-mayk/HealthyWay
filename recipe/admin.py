from django.contrib import admin

from recipe.models import Recipe


@admin.register(Recipe)
class AdminPosts(admin.ModelAdmin):
    list_display = [
        'title',
    ]
