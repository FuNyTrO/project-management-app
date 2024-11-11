from django.urls import path
from . import views  # импорт представлений из текущего приложения

urlpatterns = [
    path('users/', views.user_list, name='user_list'),  
    # path('<int:project_id>/', views.project_detail, name='project_detail'),  
]
