# --- jobs/forms.py ---
# NEW FILE TO CREATE!

from django import forms
from .models import Job

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        # Fields the company user can fill out
        fields = ('title', 'description', 'location', 'salary')
        # The 'company' field is set automatically in the view