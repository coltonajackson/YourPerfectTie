from django.contrib import admin
from shop.models import user, item, ordered_item

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	pass

class ItemAdmin(admin.ModelAdmin):
	pass

class OrderedItemAdmin(admin.ModelAdmin):
	pass

admin.site.register(user, UserAdmin)
admin.site.register(item, ItemAdmin)
admin.site.register(ordered_item, OrderedItemAdmin)