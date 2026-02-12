from django.db import models
from django.contrib.auth.models import User


class UserForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    form_data = models.JSONField()

    def __str__(self):
        return f"{self.user} - {self.title}"

class ShareForm(models.Model):
    form = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.form} - {self.shared_user}"
        # Add this at the bottom of your existing models.py
class FormSubmission(models.Model):
    # Linking to the specific UserForm you already created
    form = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='submissions')
    user_name = models.CharField(max_length=255)
    # This 'uploaded_file' will automatically go to S3 once we update settings.py
    uploaded_file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user_name} for {self.form.title}"