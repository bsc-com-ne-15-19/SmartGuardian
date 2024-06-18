from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'employee_id', 'is_staff', ] 
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('employee_id',)}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('employee_id',)}),)

admin.site.register(CustomUser, CustomUserAdmin)