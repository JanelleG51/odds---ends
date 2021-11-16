from django.contrib import admin
from .models import Wine, Case, Category

# Register your models here.
admin.site.register(Wine)
admin.site.register(Case)
admin.site.register(Category)
