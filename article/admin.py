from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'created')
    list_filter = ('created', 'updated', 'owner')
    serach_fields = ('title', 'body')
    raw_id_fields = ('owner',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('body',)
    raw_id_fields = ('article', 'owner')
