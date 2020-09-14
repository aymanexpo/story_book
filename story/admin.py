from django.contrib import admin

# Register your models here.
from .models import Story,Category

admin.site.register(Story)
admin.site.register(Category)