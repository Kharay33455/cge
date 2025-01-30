from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(InnerLink)
admin.site.register(ServiceHeader)
admin.site.register(Company)
admin.site.register(Chat)
admin.site.register(Message)