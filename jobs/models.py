# --- jobs/models.py ---

from django.db import models
from accounts.models import Company # Import the Company model

class Job(models.Model):
    # Link the job to a specific company (Foreign Key)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title