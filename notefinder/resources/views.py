from django.shortcuts import render, get_object_or_404, redirect
from resources.models import ResourceItem, Course, ResourceURL
from django.db.models import Q
from django.http import FileResponse
from django.utils.text import slugify
from resources.forms import ResourceItemForm, ResourceURLForm
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
    url_resources = ResourceURL.objects.all()

    query_string = request.GET.get('search_q')
    if query_string:
        resources = resources.filter(
            Q(course__code__icontains=query_string)|
            Q(course__name__icontains=query_string)|
            Q(description__icontains=query_string) |
            Q(file__icontains=query_string)|
            Q(tags__name__in=[query_string])
            ).distinct()
        url_resources = url_resources.filter(
            Q(course__code__icontains=query_string)|
            Q(course__name__icontains=query_string)|
            Q(description__icontains=query_string) |
            Q(url__icontains=query_string)|
            Q(tags__name__in=[query_string])
            ).distinct()
    template_name = "resources/search_results.html"
    context = {
        "resources": resources,
        "url_resources":url_resources,
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



def add_resource(request):
    template_name = "resources/add_resource.html"
    return render(request, template_name)


def add_resource_item(request):
    if request.method == "POST":
        form = ResourceItemForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.save()
            form.save_m2m()
            return redirect('HomePage')

    form = ResourceItemForm()
    template_name = "resources/add_resource_item.html"
    context = {
        'form':form,
    }
    return render(request, template_name, context)


def resource_item_detail(request, pk, slug):
    resource = get_object_or_404(ResourceItem, pk=pk)
    template_name = 'resources/resource_item_detail.html'
    context = {
        'resource':resource
    }
    return render(request, template_name, context)


def resource_url_detail(request, pk):
    resource = get_object_or_404(ResourceURL, pk=pk)
    template_name = 'resources/resource_url_detail.html'
    context = {
        'resource':resource
    }
    return render(request, template_name, context)




def add_resource_url(request):
    if request.method == "POST":
        form = ResourceURLForm(request.POST)
        print(form.errors)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.save()
            form.save_m2m()
            return redirect('HomePage')

    form = ResourceURLForm()
    template_name = "resources/add_resource_url.html"
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def course_detail(request, course_code):
    course = get_object_or_404(Course, code=course_code)
    resources = ResourceItem.objects.all().filter(course__code=course_code)
    url_resources = ResourceURL.objects.all().filter(course__code=course_code)
    template_name = "resources/course_detail.html"
    context = {
        "course":course,
        "resources":resources,
        "url_resources":url_resources,
    }
    return render(request, template_name, context)

def all_resource(request):
    all_resource_item = ResourceItem.objects.all()
    all_resource_url = ResourceURL.objects.all()
    template_name = "resources/all_resource.html"
    context = {
        'all_resource_item':all_resource_item,
        'all_resource_url':all_resource_url
    }
    return render(request, template_name, context)


def course_list(request):
    courses = Course.objects.all()
    template_name = "resources/course_list.html"
    context = {
        "courses":courses,
    }
    return render(request, template_name,context)

