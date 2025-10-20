from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from hangarinorg.models import Priority, Category, Task, Note, SubTask

class Command(BaseCommand):
    help = 'Create initial data for Hangarin application'
    
    def handle(self, *args, **kwargs):
        self.create_priorities()
        self.create_categories()
        self.create_tasks(25)
        self.create_notes(40)
        self.create_subtasks(60)
    
    def create_priorities(self):
        priorities = ['High', 'Medium', 'Low', 'Critical', 'Optional']
        for priority_name in priorities:
            Priority.objects.get_or_create(name=priority_name)
        self.stdout.write(self.style.SUCCESS('Priorities created successfully.'))
    
    def create_categories(self):
        categories = ['Work', 'School', 'Personal', 'Finance', 'Projects']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)
        self.stdout.write(self.style.SUCCESS('Categories created successfully.'))
    
    def create_tasks(self, count):
        fake = Faker()
        
        for _ in range(count):
            # Create task with realistic data
            Task.objects.create(
                Title=fake.sentence(nb_words=5),  # Generates: "Modern require follow administration indeed."
                description=fake.paragraph(nb_sentences=3),  # Generates a paragraph with 3 sentences
                deadline=fake.date_between(start_date='today', end_date='+30d'),  # Deadline within next 30 days
                status=fake.random_element(elements=["pending", "In Progress", "Completed"]),
                task_category=Category.objects.order_by('?').first(),  # Random category
                task_priority=Priority.objects.order_by('?').first()   # Random priority
            )
        
        self.stdout.write(self.style.SUCCESS(f'{count} tasks created successfully.'))
    
    def create_notes(self, count):
        fake = Faker()
        
        for _ in range(count):
            Note.objects.create(
                related_task=Task.objects.order_by('?').first(),  # Random task
                content=fake.paragraph(nb_sentences=4)  # Longer paragraph for notes
            )
        
        self.stdout.write(self.style.SUCCESS(f'{count} notes created successfully.'))
    
    def create_subtasks(self, count):
        fake = Faker()
        
        for _ in range(count):
            SubTask.objects.create(
                parent_task=Task.objects.order_by('?').first(),  # Random parent task
                title=fake.sentence(nb_words=4),  # Shorter title for subtasks
                status=fake.random_element(elements=["pending", "In Progress", "Completed"])
            )
        
        self.stdout.write(self.style.SUCCESS(f'{count} subtasks created successfully.'))