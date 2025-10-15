"""
URL configuration for hangarinsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hangarinorg.views import (
    HomePageView, PriorityListView, CategoryList, TaskList, NoteList, SubTaskList, 
    PriorityCreateView, CategoryCreateView, TaskCreateView, NoteCreateView, SubTaskCreateView, 
    PriorityUpdateView, CategoryUpdateView, TaskUpdateView, NoteUpdateView, SubTaskUpdateView, 
    PriorityDeleteView, CategoryDeleteView, TaskDeleteView,NoteDeleteView, SubTaskDeleteView
)
from hangarinorg.views import index_view



urlpatterns = [
    
    path('', index_view, name='home'),  # Serves index.html at root URL


    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('priority_list',PriorityListView.as_view(), name='priority-list' ),
    path('category_list',CategoryList.as_view(), name='category-list' ),
    path('task_list',TaskList.as_view(), name='task-list' ),
    path('note_list',NoteList.as_view(), name='note-list' ),
    path('subtask_list',SubTaskList.as_view(), name='subtask-list' ),
    
    # CreateView
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),
    path('subtask_list/add', SubTaskCreateView.as_view(), name='subtask-add'),

    # UPDATE views
    path('priority_list/edit/<int:pk>/', PriorityUpdateView.as_view(), name='priority-edit'),
    path('category_list/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category-edit'),
    path('task_list/edit/<int:pk>/', TaskUpdateView.as_view(), name='task-edit'),
    path('note_list/edit/<int:pk>/', NoteUpdateView.as_view(), name='note-edit'),
    path('subtask_list/edit/<int:pk>/', SubTaskUpdateView.as_view(), name='subtask-edit'),


    # Delete 
    path('priority_list/delete/<int:pk>/', PriorityDeleteView.as_view(), name='priority-delete'),
    path('category_list/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('task_list/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('note_list/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    path('subtask_list/delete/<int:pk>/', SubTaskDeleteView.as_view(), name='subtask-delete'),



     
]
