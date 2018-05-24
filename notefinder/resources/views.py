from django.shortcuts import render, get_object_or_404, redirect
from resources.models import ResourceItem, Course
from django.db.models import Q
from django.http import FileResponse
from django.utils.text import slugify
import os

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
            Q(description__icontains=query_string) |
            Q(tags__name__in=[query_string])
            ).distinct()
    template_name = "resources/search_results.html"
    context = {
        "resources": resources
    }
    return render(request, template_name, context)


def download_item(request, id):
    item = get_object_or_404(ResourceItem, pk=id)
    file_name, file_extension = os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.file.file, 
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.file.name)[:100], file_extension)
    return response


def preview_item(request, id):
    item = get_object_or_404(ResourceItem, pk=id)
    file_name, file_extension = os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    
    print("---------------------{}{}, {}".format(item.file.file.name,file_name, file_extension))
    file = item.file
    return redirect('/media/' + file.name)


