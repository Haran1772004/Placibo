from django.contrib import admin
from django.urls import path, include
from . import views  # Added this import

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Root path for testing CI/CD - Added this line
    path('', views.home, name='home'), 

    # Existing API paths
    path('api/accounts/', include('accounts.urls')),
    path('api/forms/', include('forms.urls')),
]