from django.urls import path
from resources.views import home, search, download_item, preview_item, add_resource_item

urlpatterns = [
    path('', home, name = "HomePage"),
    path('search', search, name = "Search"),
    path('download/<int:id>', download_item, name="Download"),
    path('preview/<int:id>', preview_item, name = "Preview"),
    path('add_resource/', add_resource_item, name="AddResource"),
]
