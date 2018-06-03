"""notefinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import *
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ResourceURLSitemap, ResourceItemSitemap, CourseSitemap, DeptSemSitemap

sitemaps = {
    'resources-item': ResourceItemSitemap,
    'resources-url' : ResourceURLSitemap,
    'courses'       : CourseSitemap,
    'departments-and-semester' : DeptSemSitemap,
    }

sitemap_urls = [
            path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                name='django.contrib.sitemaps.views.sitemap'),

    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("resources.urls")),
    path('taggit_autosuggest', include('taggit_autosuggest.urls')),
    path('who-own-these-notes/', TemplateView.as_view(template_name="notes_ownership.html"), name="NotesOwnership"),
]

urlpatterns += sitemap_urls

urlpatterns += static(MEDIA_URL,
                 document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL,
                  document_root=STATIC_ROOT)