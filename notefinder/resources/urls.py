from django.urls import path
from resources.views import home, search, download_item, preview_item, add_resource_item, add_resource_url, add_resource, resource_item_detail, course_detail, course_list, all_resource, resource_url_detail, deptsem_list, deptsem_detail

urlpatterns = [
    path('', home, name = "HomePage"),
    path('search', search, name = "Search"),
    path('download/<int:id>', download_item, name="Download"),
    path('preview/<int:id>', preview_item, name = "Preview"),
    path('add_resource/', add_resource, name = "AddResource"),
    path('add-notes/', add_resource_item, name="AddResourceFile"),
    path('add-notes-urls/', add_resource_url, name="AddResourceURL"),
    path('notes-detail/<slug:slug>/<int:pk>/', resource_item_detail, name="ResourceItemDetail"),
    path('notes-url-detail/<int:pk>/', resource_url_detail, name="ResourceURLDetail"),
    path('course_detail/<str:course_code>/', course_detail, name = "CourseDetail"),
    path('department-and-semester-details/<int:pk>', deptsem_detail, name="DeptSemDetail"),
    path('course_list/', course_list, name="CourseList"),
    path('departments_and_semesters/', deptsem_list, name = "DeptSemList" ),
    path('all_resource/', all_resource, name="AllResource"),
]
