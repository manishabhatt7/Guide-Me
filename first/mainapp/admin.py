

# Register your models here.

from django.contrib import admin
from .models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display=('id', 'firstname','age','gender','address','price','language','subject')

admin.site.register(Guide,GuideAdmin)