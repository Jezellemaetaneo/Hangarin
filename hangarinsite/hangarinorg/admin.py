from django.contrib import admin

# Register your models here.
from .models import Task, Substask, Category, Priority, Note

admin.site.register(Task)
admin.site.register(Substask)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Note)
