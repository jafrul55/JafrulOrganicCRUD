from django.contrib import admin
from .models import OrganicStoreModel
# Register your models here.

class OrganicFoodAdmin(admin.ModelAdmin):
        list_display = ['id','product_name','farmer_name','category','collected_food','last_collected']

admin.site.register(OrganicStoreModel,OrganicFoodAdmin)