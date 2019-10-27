from __future__ import unicode_literals

from django.urls import path
from courses import views

urlpatterns = [
	path('', views.index, name='courses_index'),
	path('<slug>', views.details, name='details'),
    path('inscricao/<slug:slug>/', views.enrollment, name='courses_enrollment'),
	path('cancelar-inscricao/<slug:slug>/', views.undo_enrollment, name='courses_undo_enrollment'),
	path('anuncios/<slug:slug>/', views.announcements, name='courses_announcements'),
	path('show_anuncios/<slug:slug>/<int:pk>', views.show_announcement, name='courses_show_announcement'),


]