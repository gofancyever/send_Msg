from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_info

class User_infoInline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = 'User_info'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (User_infoInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

