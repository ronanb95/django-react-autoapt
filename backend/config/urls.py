from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings_api/', include('listings_api.urls', namespace='listings_api')),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
