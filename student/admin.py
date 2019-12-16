from django.contrib import admin
# Register your models here.

from .models import StudentApp, StudentReg, Staff, Department

admin.site.register(StudentApp)
admin.site.register(StudentReg)
admin.site.register(Staff)
admin.site.register(Department)


