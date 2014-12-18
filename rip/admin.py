from django.contrib import admin
from rip.models import Service, Operation, TestCase

# Register your models here.

admin.site.register(Service)
admin.site.register(Operation)
admin.site.register(TestCase)


