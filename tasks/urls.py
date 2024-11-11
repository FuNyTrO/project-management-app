from django.urls import path
from . import views  # импорт представлений из текущего приложения

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),  
    # path('<int:project_id>/', views.project_detail, name='project_detail'),  
]
