from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('username','email')
    list_display = ('username','email')