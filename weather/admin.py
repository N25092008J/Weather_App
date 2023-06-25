from django.contrib import admin

# Register your models here.

from .models import cities # importing classes from other files

admin.site.register(cities) # registering a table