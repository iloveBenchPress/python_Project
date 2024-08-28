from django.contrib import admin
from .models import Review



class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Review,TodoAdmin)

