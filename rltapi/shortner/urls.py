from django.urls import path
from . import views

urlpatterns = [
    path('get_urls_list/', views.URLs_list),
    path('', views.click_test_redirection_view)
]