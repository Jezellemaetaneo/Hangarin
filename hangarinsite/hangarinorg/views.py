
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from hangarinorg.forms import PriorityForm, CategoryForm, TaskForm, NoteForm, SubTaskForm
from django.urls import reverse_lazy
from hangarinorg.models import Priority, Category, Task, Note, SubTask 
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render



def index_view(request):
    return render(request, 'home.html')

 

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Summary counts
        context["total_task"] = Task.objects.count()
        context["total_note"] = Note.objects.count()
        context["total_subtask"] = SubTask.objects.count()
        context["total_category"] = Category.objects.count()
        context["total_priority"] = Priority.objects.count()

        # Extra context for dashboard
        today = timezone.now().date()

        # Show tasks with deadlines in the next 7 days
        context["near_deadline_tasks"] = Task.objects.filter(deadline__gte=today, deadline__lte=today + timezone.timedelta(days=7)).order_by("deadline")

        # Show most recent tasks (e.g. last 5 created)
        context["recent_tasks"] = Task.objects.order_by("-created_at")[:5]

        return context


#LISTVIEW
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5 

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(name__icontains=query)
                ) 
        return qs 

    
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(name__icontains=query)
                ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name"

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "task_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(Title__icontains=query) |
                Q(status__icontains=query) |
                Q(task_priority__name__icontains=query) |  # ForeignKey lookup
                Q(task_category__name__icontains=query) |  # ForeignKey lookup
                Q(deadline__icontains=query)  # This might still cause issues with DateField
            ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["Title", "status", "task_priority", "task_category", "deadline"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "Title"



class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = "note_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(related_task__Title__icontains=query) |  # CHANGED: task__title → related_task__Title
                Q(content__icontains=query)
            ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["related_task", "content"]  # CHANGED: "task" → "related_task"
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "related_task"
    
from django.db.models import Q

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = "subtask_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(parent_task__Title__icontains=query) |  # Task title
                Q(title__icontains=query) |               # SubTask title
                Q(status__icontains=query) |              # SubTask status
                Q(parent_task__deadline__icontains=query) |  # Parent task deadline
                Q(parent_task__task_priority__name__icontains=query) |  # Parent task priority
                Q(parent_task__task_category__name__icontains=query)    # Parent task category
            ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["title", "status", "parent_task"]  # Only use fields that exist in SubTask model
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"


#CREATEVIEW
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')


#UPDATE 
class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

#DELETE
class PriorityDeleteView(DeleteView):  # Make sure the class name matches
    model = Priority
    template_name = "priority_del.html"  # Your template
    success_url = reverse_lazy('priority-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html' 
    success_url = reverse_lazy('category-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html' 
    success_url = reverse_lazy('task-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html' 
    success_url = reverse_lazy('note-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html' 
    success_url = reverse_lazy('subtask-list')
