from django.contrib import admin

from .models import ObjectViewed, UserSession



@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
     list_display = [ 'user' , 'ip_address' , 'active', 'ended','timestamp' ]
     


admin.site.register(ObjectViewed)
#admin.site.register(UserSession)