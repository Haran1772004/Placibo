from django.contrib import admin
from django.urls import path, include
from . import views # Correctly imported

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Root path for testing CI/CD
    path('', views.home, name='home'),

    # Existing API paths
    path('api/accounts/', include('accounts.urls')),
    path('api/forms/', include('forms.urls')),
]