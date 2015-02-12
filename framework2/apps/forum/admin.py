from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(ChildCategory)

admin.site.register(Thread)
admin.site.register(Answer)
admin.site.register(Comment)