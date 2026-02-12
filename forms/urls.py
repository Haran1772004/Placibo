from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import UserFormViewSet, ShareFormViewSet
from .views import export_submissions_to_excel

router = DefaultRouter()
router.register(r'user-forms', UserFormViewSet, basename='user-form')
router.register(r'share-forms', ShareFormViewSet, basename='share-form')

urlpatterns = [
    # Custom path for Excel Task
    path('export-excel/', export_submissions_to_excel, name='export_excel'),
]

# Add the router URLs
urlpatterns += router.urls