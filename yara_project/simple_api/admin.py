from django.contrib import admin

from models import Purchase

@admin.register(Purchase)
class BugDetailAdmin(admin.ModelAdmin):
    list_display = ('name','datetime')
