from django.contrib import admin
from .models import CourseInfo, CourseAdd

# Register your models here.
@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['theme', 'course_name', 'departure', 'arrival', 'hours', 'mins', 'introduce']
    list_per_page = 10

@admin.register(CourseAdd)
class CourseAddAdmin(admin.ModelAdmin):
    list_display = ['courseinfo', 'course_name', 'departure', 'arrival', 'introduce']