from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'bio',
    )
    list_editable = ('role',)
    search_fields = (
        'username',
        'bio',
    )
    list_filter = ('role',)
    empty_value_display = '-пусто-'
