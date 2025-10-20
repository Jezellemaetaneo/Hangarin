from django.contrib import admin
from .models import Priority, Category, Task, Note, SubTask

# Inline configurations for Task admin
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'status')
    show_change_link = True

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ('content', 'created_at')
    readonly_fields = ('created_at',)

# Admin configurations
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Title', 'status', 'deadline', 'task_priority', 'task_category', 'created_at')
    list_filter = ('status', 'task_priority', 'task_category', 'created_at')
    search_fields = ('Title', 'description')
    date_hierarchy = 'deadline'
    inlines = [SubTaskInline, NoteInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('related_task', 'content_preview', 'created_at')
    list_filter = ('created_at', 'related_task')
    search_fields = ('content', 'related_task__Title')
    
    def content_preview(self, obj):
        return obj.content[:75] + "..." if len(obj.content) > 75 else obj.content
    content_preview.short_description = "Content Preview"

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task', 'created_at')
    list_filter = ('status', 'created_at', 'parent_task')
    search_fields = ('title', 'parent_task__Title')
    
    def parent_task_name(self, obj):
        return obj.parent_task.Title
    parent_task_name.short_description = "Parent Task"