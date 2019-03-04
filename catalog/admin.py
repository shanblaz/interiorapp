from django.contrib import admin

# Register your models here.
from catalog.models import bedroom, kitchen


admin.site.register(kitchen)
admin.site.register(bedroom)


