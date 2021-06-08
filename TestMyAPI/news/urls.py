from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:id>/', views.project_detail),
    path('projects/projects_filtered/<int:pt>/', views.project_filter),
    path('projects/NewProjectRequest/', views.NewProjectRequest),
    path('projects/NewConsultRequest/', views.NewConsultRequest),
    path('projects/setupNewProject/', views.setupNewProject),
]