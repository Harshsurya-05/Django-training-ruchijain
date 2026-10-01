from django.contrib import admin
from dbapp.models import customer
from dbapp.models import order
from dbapp.models import client
# Register your models here.


admin.site.register(client)
admin.site.register(customer)
admin.site.register(order)