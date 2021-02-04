from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0

#class CommentInline(admin.TabularInline):
#    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
