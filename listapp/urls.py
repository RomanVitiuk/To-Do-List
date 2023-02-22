from django.urls import path
from .views import *


urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('tdl/', TdlView.as_view(), name='tdl'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('tasks-list/', UserTasksListView.as_view(), name='index'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(
        extra_context={'title': 'Delete Page'}
    ), name='delete'),
    path('add-task/', UserAddTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='show_task'),
]
