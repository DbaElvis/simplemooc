# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Course, Enrollment, Announcement, Comment


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment])

# class EnrollmentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'course']









