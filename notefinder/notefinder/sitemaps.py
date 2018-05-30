from django.contrib.sitemaps import Sitemap
from resources.models import Course, ResourceItem, ResourceURL, DeptSem


class ResourceItemSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ResourceItem.objects.all()

class ResourceURLSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ResourceURL.objects.all()

class CourseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Course.objects.all()

class DeptSemSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return DeptSem.objects.all()
