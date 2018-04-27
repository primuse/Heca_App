from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='home'),
    path('project/<int:post_id>/', views.project_detail, name='detail'),
    path('home/project_new/', views.project_new, name='new'),
    path('project/<int:post_id>/project_new/', views.project_new, name='new'),
    path('home/project_new/project/<int:post_id>/', views.project_new, name='new'),
    path('project/<int:post_id>/edit/', views.project_edit, name='project_edit' ),
    path('project/<int:post_id>/start/', views.project_start, name='project_start'),
    path('project/<int:post_id>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:post_id>/complete', views.project_complete, name='project_complete'),

]