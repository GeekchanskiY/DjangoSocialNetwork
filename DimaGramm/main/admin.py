from django.contrib import admin
from .models import DMTUser
# Register your models here.


@admin.register(DMTUser)
class DMTUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    fields = ('email', 'is_staff', 'is_active', 'date_joined', 'user_image', 'username')
    search_fields = [
        'username',
        'email'
    ]
