from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Book,Item,Cart
from .siganls import create_total_price

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','role')
    list_filter = ('email', 'is_staff', 'is_active','role')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','role' ,'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
# @admin.register(Item)
# class ChildAdmin(admin.ModelAdmin):
#     exclude = ('total_price',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.site_header = 'Book Store'