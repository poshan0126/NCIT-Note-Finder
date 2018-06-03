from django.contrib.sitemaps import Sitemap
from resources.models import Course, ResourceItem, ResourceURL, DeptSem


class ResourceItemSitemap(Sitemap):


    def items(self):
        return ResourceItem.objects.all()

class ResourceURLSitemap(Sitemap):


    def items(self):
        return ResourceURL.objects.all()

class CourseSitemap(Sitemap):


    def items(self):
        return Course.objects.all()

class DeptSemSitemap(Sitemap):

    def items(self):
        return DeptSem.objects.all()
