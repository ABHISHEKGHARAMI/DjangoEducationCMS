from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Course
# Create your views here.


# creating the crude for the course
class CourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'
    
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

# using the different mixing for the crud operation
class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
    
class OwnerEditMixin:
    def get_queryset(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
# purpose of using the different type of the mixin
# 1: Multiple feature of the data
# 2: Use the particular feature of the data for the different class
    
class OwnerCourseMixin(OwnerMixin,LoginRequiredMixin,PermissionRequiredMixin):
    model = Course
    fields = ['subject','title','slug','overview']
    success_url = reverse_lazy('manage_course_list')
    
    
class OwnerCourseEditMixin(OwnerCourseMixin,OwnerMixin):
    template_name = 'courses/manage/course/form.html'
    
class ManageCourseListView(OwnerCourseMixin,ListView):
    template_name = 'courses/manage/course/list.html'
    
class CourseCreateView(OwnerCourseEditMixin,CreateView):
    pass

class CourseUpdateView(OwnerCourseMixin,UpdateView):
    pass

class CourseDeleteView(OwnerCourseMixin,DeleteView):
    template_name = 'courses/manage/course/delete.html'