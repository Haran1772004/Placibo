from django.contrib import admin
from .models import UserForm, ShareForm, FormSubmission

# This allows you to create/edit Forms in the admin panel
admin.site.register(UserForm)

# This allows you to manage shared forms
admin.site.register(ShareForm)

# This is CRITICAL for Task 1: You can now manually upload a file to S3 
# through the admin panel to test if your Task 1 logic works!
admin.site.register(FormSubmission)