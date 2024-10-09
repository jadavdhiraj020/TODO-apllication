from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CategoryListView,
    TagListView,
    AddCommentView,
    TaskByCategoryView,
    TaskByTagView,  # Import the new view for tags
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tasks/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('categories/<int:pk>/', TaskByCategoryView.as_view(), name='tasks_by_category'),  # Category filtering
    path('tags/<int:pk>/', TaskByTagView.as_view(), name='tasks_by_tag'),  # Add this line for tag filtering
]
