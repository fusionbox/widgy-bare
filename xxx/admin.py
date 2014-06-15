from django.contrib import admin

from widgy.admin import WidgyAdmin

from .models import Owner


admin.site.register(Owner, WidgyAdmin)
