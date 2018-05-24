from django.shortcuts import render
from resources.models import ResourceItem, Course
from django.db.models import Q

# Create your views here.

def home(request):
    courses = Course.objects.all()
    resources = ResourceItem.objects.all()
    template_name = "home.html"
    context = {
        "courses":courses,
        "resources":resources,

    }
    return render(request, template_name, context)


def search(request):
    resources = ResourceItem.objects.all()
    query_string = request.GET.get('search_q')
    if query_string:
        resources = resources.filter(
            Q(course__code__icontains=query_string)|
            Q(course__name__icontains=query_string)|
            Q(description__icontains=query_string)
            ).distinct()
    template_name = "resources/search_results.html"
    context = {
        "resources": resources
    }
    return render(request, template_name, context)

