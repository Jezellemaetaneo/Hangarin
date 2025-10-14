from django.core.management.base import BaseCommand
from faker import Faker
from Hangarin.models import Priority, Category, Task, Note, SubTask
from django.utils import timezone
import random  


class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.ensure_defaults()
        self.create_Task(100)
        self.create_Notes(100)
        self.create_SubTask(100)

    def ensure_defaults(self):
        if not Category.objects.exists():
            Category.objects.create(name="Work")
            Category.objects.create(name="School")
            Category.objects.create(name="Personal")
            Category.objects.create(name="Finance")
            Category.objects.create(name="Projects")

        if not Priority.objects.exists():
            Priority.objects.create(name="high")
            Priority.objects.create(name="medium")
            Priority.objects.create(name="low")
            Priority.objects.create(name="critical")
            Priority.objects.create(name="optional")


    def create_Task(self, count):
        fake = Faker()
        categories = Category.objects.all()
        priorities = Priority.objects.all()

        for _ in range(count):
            Task.objects.create(
                Title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                task_category=random.choice(categories),
                task_priority=random.choice(priorities)
            )

        self.stdout.write(self.style.SUCCESS('Tasks created successfully.'))

    def create_Notes(self, count):
        fake = Faker()
        tasks = Task.objects.all()

        for _ in range(count):
            Note.objects.create(
                related_task=random.choice(tasks),
                content=fake.paragraph(nb_sentences=4)
            )

        self.stdout.write(self.style.SUCCESS('Notes created successfully.'))

    def create_SubTask(self, count):
        fake = Faker()
        tasks = Task.objects.all()

        for _ in range(count):
            SubTask.objects.create(
                parent_task=random.choice(tasks),
                title=fake.sentence(nb_words=4),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
            )

        self.stdout.write(self.style.SUCCESS('Subtasks created successfully.'))
