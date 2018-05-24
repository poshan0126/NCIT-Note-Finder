from django.contrib import admin
from resources.models import DeptSem, Faculty, Course, ResourceItem
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    '''
        Admin View for Course
    '''
    list_display = ('name', 'code',)


class ResourceItemAdmin(admin.ModelAdmin):
    '''
        Admin View for ResourceItem
    '''
    list_display = ('file', 'description',)


admin.site.register(ResourceItem, ResourceItemAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DeptSem)
admin.site.register(Faculty)