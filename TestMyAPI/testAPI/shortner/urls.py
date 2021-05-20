from django.urls import path
from . import views

urlpatterns = [
    path('', views.URLs_list),
    path('test_click_view', views.click_test_view, name='test_click_view'),
    path('<str:url_hash>', views.click_test_redirection_view, name='click_test_redirection_view'),
    path('add_new_link', views.add_new_short_link, name='add_new_short_link')
]