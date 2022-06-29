from django.contrib import admin
from recommend.models import Shoes as ShoesModel
from recommend.models import Brand as BrandModel
# Register your models here.

admin.site.register(ShoesModel)
admin.site.register(BrandModel)
