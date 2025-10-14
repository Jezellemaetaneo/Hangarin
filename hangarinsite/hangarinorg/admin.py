from django.contrib import admin



from .models import Priority, Category, Task, Note, SubTask

class SubTaskInline(admin.TabularInline):
    model = SubTask
    fk_name = "parent_task"
    extra = 1
    fields = ("title", "status")
    show_change_link = True

class NoteInline(admin.StackedInline):
    model = Note
    fk_name = "related_task"
    extra = 1
    fields = ("content", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Title', 'status', 'task_priority', 'task_category', 'deadline')
    list_filter = ('status', 'task_priority', 'task_category')
    search_fields = ('Title', 'description')
    inlines = [SubTaskInline, NoteInline]
   

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task_name')
    def parent_task_name(self, obj):
        return obj.parent_task.Title if obj.parent_task else "—"
    parent_task_name.short_description = 'Parent Task'
    list_filter =  ('status',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)         
    search_fields = ('name',) 

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)         
    search_fields = ('name',) 

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('related_task', 'content', 'created_at')
    list_filter = ('created_at',) 
    search_fields = ('content',)
