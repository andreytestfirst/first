from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# admin.site.register(PersonModel)
admin.site.register(StatusModel)
admin.site.register(CourseModel)
admin.site.register(AddressModel)
admin.site.register(CoursePerformanceModel)
admin.site.register(PerformanceModel)


@admin.register(PersonModel)
class PersonModelAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'address')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )
    list_display_links = ('email', 'first_name', 'last_name',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'address',)
    list_editable = ('username',)
    list_filter = ('username','email',)

