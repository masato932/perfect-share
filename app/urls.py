from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/<int:year>/<int:month>/<int:day>/', views.AddView.as_view(), name='add'),
    path('task/<int:pk>/edit/<int:year>/<int:month>/<int:day>/', views.TaskEditView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/<int:year>/<int:month>/<int:day>/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/add/<int:year>/<int:month>/<int:day>/', views.TaskAddView.as_view(), name='task_add'),
]