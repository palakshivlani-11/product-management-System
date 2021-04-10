from django.contrib import admin
from .models import *

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('modelno','size','price')
    search_fields = ('modelno','size','water','gas','air','wpf','density','vescosity','temp','pressure','distance','price')
    list_per_page = 15


admin.site.register(product,productAdmin)