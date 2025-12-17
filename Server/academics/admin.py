from django.contrib import admin
from .models import Department, Course, Class, CourseAssignment ,Topic, TeachingProgress

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(CourseAssignment)
admin.site.register(Topic)
admin.site.register(TeachingProgress)
