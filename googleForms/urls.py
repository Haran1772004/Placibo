from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Root path for testing CI/CD
    

    # Existing API paths
    path('api/accounts/', include('accounts.urls')),
    path('api/forms/', include('forms.urls')),
]