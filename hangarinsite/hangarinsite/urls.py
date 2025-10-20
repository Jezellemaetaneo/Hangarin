from django.contrib import admin
from django.urls import path
from hangarinorg.views import (
    HomePageView, PriorityListView, CategoryList, TaskList, NoteList, SubTaskList, 
    PriorityCreateView, CategoryCreateView, TaskCreateView, NoteCreateView, SubTaskCreateView, 
    PriorityUpdateView, CategoryUpdateView, TaskUpdateView, NoteUpdateView, SubTaskUpdateView, 
    PriorityDeleteView, CategoryDeleteView, TaskDeleteView, NoteDeleteView, SubTaskDeleteView
)
from hangarinorg.views import index_view

urlpatterns = [
    path('', index_view, name='home'),  # Serves index.html at root URL
    path("admin/", admin.site.urls),
    
    # List views - ADD TRAILING SLASHES
    path('priority_list/', PriorityListView.as_view(), name='priority-list'),  # Added /
    path('category_list/', CategoryList.as_view(), name='category-list'),      # Added /
    path('task_list/', TaskList.as_view(), name='task-list'),                  # Added /
    path('note_list/', NoteList.as_view(), name='note-list'),                  # Added /
    path('subtask_list/', SubTaskList.as_view(), name='subtask-list'),         # Added /
    
    # CreateView - ADD TRAILING SLASHES
    path('priority_list/add/', PriorityCreateView.as_view(), name='priority-add'),    # Added /
    path('category_list/add/', CategoryCreateView.as_view(), name='category-add'),    # Added /
    path('task_list/add/', TaskCreateView.as_view(), name='task-add'),                # Added /
    path('note_list/add/', NoteCreateView.as_view(), name='note-add'),                # Added /
    path('subtask_list/add/', SubTaskCreateView.as_view(), name='subtask-add'),       # Added /

    # UPDATE views - These are correct
    path('priority_list/edit/<int:pk>/', PriorityUpdateView.as_view(), name='priority-edit'),
    path('category_list/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category-edit'),
    path('task_list/edit/<int:pk>/', TaskUpdateView.as_view(), name='task-edit'),
    path('note_list/edit/<int:pk>/', NoteUpdateView.as_view(), name='note-edit'),
    path('subtask_list/edit/<int:pk>/', SubTaskUpdateView.as_view(), name='subtask-edit'),

    # Delete views - These are correct
    path('priority_list/delete/<int:pk>/', PriorityDeleteView.as_view(), name='priority-delete'),
    path('category_list/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('task_list/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('note_list/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    path('subtask_list/delete/<int:pk>/', SubTaskDeleteView.as_view(), name='subtask-delete'),
]