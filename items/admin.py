from django.contrib import admin
from .models import Item, Comment

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 0

class ItemAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]

admin.site.register(Item, ItemAdmin)
admin.site.register(Comment)