from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'phone_number', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname',)
    search_fields = ('name', 'user',)
