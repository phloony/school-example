from django.contrib import admin

from .models import (Parent,
                     Student,
                     StudentClass,
                     StudentParent)


admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(StudentClass)
admin.site.register(StudentParent)
