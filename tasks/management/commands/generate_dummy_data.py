from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from tasks.models import Category, Tag, UserProfile, Comment, Task
import random

class Command(BaseCommand):
    help = 'Generate dummy data for the application'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate Categories
        categories = []
        for _ in range(10):  # Create 10 categories
            category = Category(
                name=fake.word(),
                slug=fake.slug(),
                description=fake.text(max_nb_chars=200)
            )
            category.save()
            categories.append(category)

        # Generate Tags
        tags = []
        for _ in range(15):  # Create 15 tags
            tag = Tag(
                name=fake.word(),
                slug=fake.slug()
            )
            tag.save()
            tags.append(tag)

        # Generate Users
        users = []
        for _ in range(10):  # Create 10 users
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'  # Use a default password for all users
            )
            users.append(user)

            # Create UserProfile
            UserProfile.objects.create(user=user, profile_picture=None)  # You can add a dummy image path if needed

        # Generate Tasks
        tasks = []
        for _ in range(20):  # Create 20 tasks
            task = Task(
                title=fake.sentence(nb_words=6),
                description=fake.text(max_nb_chars=300),
                due_date=fake.date_time_between(start_date='now', end_date='+30d'),
                priority=random.choice([Task.HIGH, Task.MEDIUM, Task.LOW]),
                status=random.choice([Task.PENDING, Task.PROCESSING, Task.DONE]),
                completed=random.choice([True, False]),
                assigned_to=random.choice(users),
                category=random.choice(categories),
            )
            task.save()
            tasks.append(task)

            # Add random tags to the task
            for _ in range(random.randint(1, 3)):  # Randomly assign 1 to 3 tags
                task.tags.add(random.choice(tags))

            # Generate Comments for each task
            for _ in range(random.randint(0, 5)):  # Randomly create between 0 to 5 comments
                Comment.objects.create(
                    task=task,
                    author=random.choice(users),
                    content=fake.text(max_nb_chars=100),
                )

        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully!'))
