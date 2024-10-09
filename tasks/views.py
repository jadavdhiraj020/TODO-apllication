from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Task, Tag, Comment, Category


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'



class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'



class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'status', 'image', 'assigned_to', 'category', 'tags']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.assigned_to = self.request.user  # Assign the current user as the task owner
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'category', 'tags']
    template_name = 'tasks/task_form.html'

    def get_object(self, queryset=None):
        task_id = self.kwargs.get('pk')  # Use 'pk' from the URL
        return get_object_or_404(Task, pk=task_id)  # Use pk to fetch the task

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})  # Change id to pk



class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'tasks/category_list.html'


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tasks/tag_list.html'


class AddCommentView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'tasks/add_comment.html'

    def form_valid(self, form):
        task = get_object_or_404(Task, id=self.kwargs['pk'])
        form.instance.task = task
        form.instance.author = self.request.user  # Set the author of the comment to the current user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, id=self.kwargs['pk'])
        return context

class TaskByCategoryView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'  # Reuse the same template

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Task.objects.filter(category__id=category_id)  # Filter tasks by category


class TaskByTagView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'  # Reuse the same template

    def get_queryset(self):
        tag_id = self.kwargs['pk']
        return Task.objects.filter(tags__id=tag_id)  # Filter tasks by tag
