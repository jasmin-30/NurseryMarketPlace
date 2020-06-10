from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import *

User = get_user_model()
# Register your models here.
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name', 'last_name', 'admin', 'timestamp')
    list_filter = ('admin', 'timestamp')
    fieldsets = (
        ('Personal Details', {'fields': (('first_name', 'last_name'), ('email', 'contact'), 'password', 'address1', ('address2', 'postal_code'), ('city', 'state'))}),
        ('Permissions', {'fields': (('admin', 'active', 'staff'),)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Personal Details', {
            'classes': ('wide',),
            'fields': (
                ('first_name', 'last_name'),
                ('email', 'contact'),
                'address1',
                ('address2', 'postal_code'),
                ('city', 'state'),
                ('password1', 'password2'),
                'active'
            )
        }
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Category)
admin.site.register(Nursery)
admin.site.register(Plants)
admin.site.register(Orders)
