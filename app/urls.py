from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/<int:year>/<int:month>/<int:day>/', views.AddView.as_view(), name='add'),
    path('task/<int:pk>/edit/<int:year>/<int:month>/<int:day>/', views.TaskEditView.as_view(), name='task_edit'),
]