
from django.urls import path,include
from .views import auth_view, home, task_create, task_detail, task_update, task_list, task_delete
app_name = 'Task'
urlpatterns = [
    path("", home,name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/",auth_view, name="auth_view"),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_update, name='task_update'),
    path('task/list', task_list, name='task_list'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]
