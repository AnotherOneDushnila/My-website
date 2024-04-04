from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo, admin.ModelAdmin)

admin.site.register(Project, admin.ModelAdmin)

admin.site.register(Education, admin.ModelAdmin)