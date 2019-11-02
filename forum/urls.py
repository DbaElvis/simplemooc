from __future__ import unicode_literals
from django.urls import path
from forum import views

urlpatterns = [
	path('', views.index, name='forum_index'),
	path('tag/<tag>/', views.index, name='forum_index_tagged'),
	path('topico/<slug>/', views.thread, name='forum_thread'),
	path('respostas/<pk>/', views.reply_correct, name='forum_reply_correct'),
	path('respostas/<pk>/', views.reply_incorrect, name='forum_reply_incorrect'),

]