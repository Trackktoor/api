from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('shortner/', include(('shortner.urls'))),
    path('login/', include('login_user.urls')),
    path('<slug:url_hash>/', include(('shortner.urls')))
]
