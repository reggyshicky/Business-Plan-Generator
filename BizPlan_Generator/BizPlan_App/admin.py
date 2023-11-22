from django.contrib import admin
from .models import BusinessPlan
from .models import ContactResponse
# Register your models here.
admin.site.register(ContactResponse)
admin.site.register(BusinessPlan)

