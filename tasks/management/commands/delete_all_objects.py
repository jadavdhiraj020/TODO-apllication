from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task, Tag, Comment, Category  # Change to your actual model

class Command(BaseCommand):
    help = 'Delete all objects of the specified model'

    def handle(self, *args, **kwargs):
        Task.objects.all().delete()  # Change to your actual model
        Tag.objects.all().delete()  # Change to your actual model
        Category.objects.all().delete()  # Change to your actual model
        Comment.objects.all().delete()  # Change to your actual model
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all objects.'))
