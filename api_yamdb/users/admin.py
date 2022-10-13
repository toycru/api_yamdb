from django.contrib.admin import ModelAdmin, register
from django.contrib.auth import get_user_model

from .forms import UserForm

User = get_user_model()


@register(User)
class UserAdmin(ModelAdmin):
    form = UserForm
    list_display = (
        'username',
        'last_name',
        'first_name',
        'email',
        'role'
    )
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'bio'
    )
