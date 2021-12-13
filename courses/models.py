from django.db import models

# Create your models here.
class CourseInfo(models.Model):

    theme = models.TextField()
    course_name = models.TextField()
    departure = models.TextField()
    arrival = models.TextField()
    hours = models.TextField()
    mins = models.TextField()
    introduce = models.TextField()

    def __str__(self):
        return self.theme

class CourseAdd(models.Model):
    courseinfo = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    course_name = models.TextField()
    departure = models.TextField()
    arrival = models.TextField()
    introduce = models.TextField()

    def __str__(self):
        return self.theme
