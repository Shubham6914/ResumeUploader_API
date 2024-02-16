from django.contrib import admin
from .models import profile
# Register your models here.


@admin.register(profile)

class AdminProfile(admin.ModelAdmin):
   list_display = ['id','name','email','gender','DOB','state','location','pimage','rdoc']