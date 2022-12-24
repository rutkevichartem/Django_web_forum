from django.contrib import admin
from .models import Task, About, Contact


admin.site.register(Task)
admin.site.register(About)
admin.site.register(Contact)