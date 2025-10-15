
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from hangarinorg.forms import PriorityForm, CategoryForm, TaskForm, NoteForm, SubTaskForm
from django.urls import reverse_lazy
from hangarinorg.models import Priority, Category, Task, Note, SubTask 
from django.db.models import Q
from django.utils import timezone
 

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

#LISTVIEW
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5 

    


class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = 5

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "task_list.html"
    paginate_by = 5

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = "note_list.html"
    paginate_by = 5

class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = "subtask_list.html"
    paginate_by = 5


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
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html' 
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
