from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_site/v1/', include('main.urls')),
    path('<slug:url_hash>', include(('shortner.urls'))),
    path('api_site/v1/shortner/', include(('shortner.urls'))),
]
