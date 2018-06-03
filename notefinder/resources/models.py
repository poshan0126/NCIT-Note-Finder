from django.db import models
from taggit_autosuggest.managers import TaggableManager
from django.shortcuts import reverse

# Create your models here.

FACULTY_CHOICES = (
    ("ST", "Science And Technology"),
    )

DEPT_SEM_CHOICES = (
    ("Software-1", "Software First Semester"),
    ("Software-2", "Software Second Semester"),
    ("Software-3", "Software Third Semester"),
    ("Software-4", "Software Fourth Semester"),
    ("Software-5", "Software Fifth Semester"),
    ("Software-6", "Software Sixth Semester"),
    ("Software-7", "Software Seventh Semester"),
    ("Software-8", "Software Eight Semester"),

    ("IT-1", "IT First Semester"),
    ("IT-2", "IT Second Semester"),
    ("IT-3", "IT Third Semester"),
    ("IT-4", "IT Fourth Semester"),
    ("IT-5", "IT Fifth Semester"),
    ("IT-6", "IT Sixth Semester"),
    ("IT-7", "IT Seventh Semester"),
    ("IT-8", "IT Eight Semester"),

    ("Computer-1", "Computer First Semester"),
    ("Computer-2", "Computer Second Semester"),
    ("Computer-3", "Computer Third Semester"),
    ("Computer-4", "Computer Fourth Semester"),
    ("Computer-5", "Computer Fifth Semester"),
    ("Computer-6", "Computer Sixth Semester"),
    ("Computer-7", "Computer Seventh Semester"),
    ("Computer-8", "Computer Eight Semester"),

    ("ELX-1", "ELX First Semester"),
    ("ELX-2", "ELX Second Semester"),
    ("ELX-3", "ELX Third Semester"),
    ("ELX-4", "ELX Fourth Semester"),
    ("ELX-5", "ELX Fifth Semester"),
    ("ELX-6", "ELX Sixth Semester"),
    ("ELX-7", "ELX Seventh Semester"),
    ("ELX-8", "ELX Eight Semester"),

    ("CIVIL-1", "CIVIL First Semester"),
    ("CIVIL-2", "CIVIL Second Semester"),
    ("CIVIL-3", "CIVIL Third Semester"),
    ("CIVIL-4", "CIVIL Fourth Semester"),
    ("CIVIL-5", "CIVIL Fifth Semester"),
    ("CIVIL-6", "CIVIL Sixth Semester"),
    ("CIVIL-7", "CIVIL Seventh Semester"),
    ("CIVIL-8", "CIVIL Eight Semester"),

    ("GS-1", "GS First Semester"),
    ("GS-2", "GS Second Semester"),
    ("GS-3", "GS Third Semester"),
    ("GS-4", "GS Fourth Semester"),
    ("GS-5", "GS Fifth Semester"),
    ("GS-6", "GS Sixth Semester"),
    ("GS-7", "GS Seventh Semester"),
    ("GS-8", "GS Eight Semester"),

    ("BCA-1", "BCA First Semester"),
    ("BCA-2", "BCA Second Semester"),
    ("BCA-3", "BCA Third Semester"),
    ("BCA-4", "BCA Fourth Semester"),
    ("BCA-5", "BCA Fifth Semester"),
    ("BCA-6", "BCA Sixth Semester"),
    ("BCA-7", "BCA Seventh Semester"),
    ("BCA-8", "BCA Eight Semester"),

    )

class Faculty(models.Model):
    faculty_of = models.CharField("Faculty of ", max_length =2, choices=FACULTY_CHOICES)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.faculty_of



class DeptSem(models.Model):
    """
    It will represent the department and semester at once.
    For Eg: Software Second Sem, IT First Sem and so on.
    """
    name = models.CharField(max_length=20, choices = DEPT_SEM_CHOICES)

    class Meta:
        verbose_name = "Department and Semester"
        verbose_name_plural = "Departments and Semesters"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DeptSemDetail', kwargs={'pk':self.pk})




class Course(models.Model):
    name = models.CharField("Course of", max_length =50)
    code = models.CharField("Course Code", max_length=6)
    description = models.TextField(null=True,blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    dept_sem = models.ManyToManyField(DeptSem)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CourseDetail', kwargs={'course_code':self.code})



class ResourceItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    file = models.FileField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    

    class Meta:
        verbose_name = "Resource Item"
        verbose_name_plural = "Resource Items"

    def __str__(self):
        return self.file.name

    def get_size(self):
        # size = self.file.size / 1000000
        return self.file.size

    def get_keywords(self):
        title = self.title
        keywords = title.replace(' ', ',')
        return keywords

    def get_absolute_url(self):
        return reverse('ResourceItemDetail', kwargs={'slug': self.slug, 'pk':self.pk})


class ResourceURL(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    

    class Meta:
        verbose_name = "Resource URL"
        verbose_name_plural = "Resource URLs"

    def __str__(self):
        return self.url
        
    def get_keywords(self):
        title = self.title
        keywords = title.replace(' ', ',')
        return keywords

    def get_absolute_url(self):
        return reverse('ResourceURLDetail', kwargs={'pk':self.pk})

