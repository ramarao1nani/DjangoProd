from django.contrib import admin
from .models import Profile
# Register your models here.

admin.site.site_header="Buy & Sell"
admin.site.site_title="ABC Buying"
admin.site.index_title="Manage ABC Buying website"

# class ProductAdmin(admin.ModelAdmin):
#     list_display=('name','price','desc')

admin.site.register(Profile)