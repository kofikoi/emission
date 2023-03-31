from django.contrib import admin
from .models import Emission, Country

#Register your models here
admin.site.register(Country)
admin.site.register(Emission)
