from django.urls import path
from . import views

urlpatterns = [
    path('all_projects', views.all_projects),
    path('all_projects/<int:id>', views.project_detail),
    path('projects/<int:id>', views.project_detail),
    path('projects_by_type/<int:pt>', views.projects_by_type),
    path('new_project_request', views.new_project_request),
    path('new_consult_request', views.new_consult_request),
    path('create_new_project', views.create_new_project),
    path('send_post_request_telegram_bot', views.send_post_request_telegram_bot),
    path('get_all_commits_in_GIT/<str:author>/<str:repos>', views.get_all_commits_in_GIT)
]