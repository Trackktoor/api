from django.urls import path
from . import views

urlpatterns = [
    path('all_shorted_urls/', views.URLs_list),
    path('short_my_url/', views.add_new_short_link),
    path('short_link_stats/<slug:short_url_hash>/', views.get_info_for_url),
    path('', views.click_test_redirection_view)
]