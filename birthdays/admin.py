from django.contrib import admin

from .models import Person, Present

admin.site.register(Person)
admin.site.register(Present)