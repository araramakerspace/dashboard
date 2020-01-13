from django.contrib import admin
from dashboard.models import  User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "email", "cpf", "password")

admin.site.register(User, UserAdmin)
#admin.site.register(Equipment)
