from django.contrib import admin

from .models import Assignment, Choice, GradedAssignment, Question
# Register your models here.

admin.site.register(Assignment)
admin.site.register(Choice)
admin.site.register(GradedAssignment)
admin.site.register(Question)