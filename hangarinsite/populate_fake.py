import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarinsite.settings')
django.setup()

from faker import Faker
from hangarinorg.models import Priority, Category, Task, Note, SubTask

fake = Faker()

# Clear old data (optional — remove if you don't want this)
Note.objects.all().delete()
SubTask.objects.all().delete()
Task.objects.all().delete()
Category.objects.all().delete()
Priority.objects.all().delete()

# 1. Create Priorities
priorities = []
for _ in range(3):
    p = Priority.objects.create(name=fake.word().capitalize())
    priorities.append(p)
print("✅ Created Priorities")

# 2. Create Categories
categories = []
for _ in range(5):
    c = Category.objects.create(name=fake.word().capitalize())
    categories.append(c)
print("✅ Created Categories")

# 3. Create Tasks
status_choices = ["pending", "In Progress", "Completed"]
for _ in range(10):
    task = Task.objects.create(
        Title=fake.sentence(nb_words=4).rstrip('.'),
        description=fake.paragraph(nb_sentences=2),
        deadline=fake.date_between(start_date="-30d", end_date="+60d"),
        status=fake.random_element(elements=status_choices),
        task_category=fake.random_element(elements=categories),
        task_priority=fake.random_element(elements=priorities)
    )

    # 4. Add Notes to some Tasks
    if fake.boolean(chance_of_getting_true=60):
        Note.objects.create(
            related_task=task,
            content=fake.paragraph(nb_sentences=2)
        )

    # 5. Add SubTasks to some Tasks
    if fake.boolean(chance_of_getting_true=50):
        for _ in range(fake.random_int(min=1, max=3)):
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3).rstrip('.'),
                status=fake.random_element(elements=status_choices)
            )

print("✅ ✅ ALL FAKE DATA INSERTED SUCCESSFULLY!")
print(f"   - {Priority.objects.count()} Priorities")
print(f"   - {Category.objects.count()} Categories")
print(f"   - {Task.objects.count()} Tasks")
print(f"   - {Note.objects.count()} Notes")
print(f"   - {SubTask.objects.count()} SubTasks")