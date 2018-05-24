from django.urls import path
from resources.views import home, search

urlpatterns = [
    path('', home, name = "HomePage"),
    path('search', search, name = "Search"),
]
