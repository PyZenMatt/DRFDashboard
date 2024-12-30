from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Include gli endpoint API
    path('auth/', include('dj_rest_auth.urls')),  # Endpoint per login/logout
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Endpoint per registrazione
]
