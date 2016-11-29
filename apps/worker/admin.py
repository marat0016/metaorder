from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Operator


# Define an inline admin descriptor for Operator model
# which acts a bit like a singleton
class OperatorInline(admin.StackedInline):
    model = Operator
    can_delete = False
    verbose_name_plural = 'operator'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (OperatorInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)