from django.contrib import admin

from .models import (Teacher,
                     Subject,
                     Class,
                     )


admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Class)
