from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email_verified_at')
    search_fields = ('user__username', 'user__email', 'phone')
    readonly_fields = ('email_verified_at',)
    
