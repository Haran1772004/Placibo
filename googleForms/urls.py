from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # The Django Admin interface
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # This connects your accounts/urls.py logic
    # Access this via: http://127.0.0.1:8000/api/accounts/users/
    path('api/accounts/', include('accounts.urls')),

    # This connects your forms/urls.py logic
    # Access this via: http://127.0.0.1:8000/api/forms/user-forms/
    path('api/forms/', include('forms.urls')),
]