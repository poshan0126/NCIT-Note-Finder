from django.urls import path
from resources.views import home, search, download_item, preview_item, add_resource_item, add_resource_url, add_resource, resource_item_detail

urlpatterns = [
    path('', home, name = "HomePage"),
    path('search', search, name = "Search"),
    path('download/<int:id>', download_item, name="Download"),
    path('preview/<int:id>', preview_item, name = "Preview"),
    path('add_resource/', add_resource, name = "AddResource"),
    path('add_resource_file/', add_resource_item, name="AddResourceFile"),
    path('add_resource_url/', add_resource_url, name="AddResourceURL"),
    path('resource_item_detail/<int:pk>/', resource_item_detail, name="ResourceItemDetail"),
]
