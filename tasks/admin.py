from django.contrib import admin
from .models import User    #import model class
# Register your models here.

@admin.register(User)   #use decorators
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
