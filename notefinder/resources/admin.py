from django.contrib import admin
from resources.models import DeptSem, Faculty, Course, ResourceItem, ResourceURL
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
    list_display = ('title', 'file', 'description',)
    prepopulated_fields = {'slug':('title',)}

class ResourceURLAdmin(admin.ModelAdmin):
    '''
        Admin View for ResourceURL
    '''
    list_display = ('title', 'url', 'description')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(ResourceURL, ResourceURLAdmin)


admin.site.register(ResourceItem, ResourceItemAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DeptSem)
admin.site.register(Faculty)