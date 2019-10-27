# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import (Course, Enrollment, Announcement, Comment, Lesson,
    Material)


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register([Announcement, Comment, Material])
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Lesson, LessonAdmin)












