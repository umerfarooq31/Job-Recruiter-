# --- accounts/forms.py ---
# NEW FILE TO CREATE!

from django import forms
from .models import User

# This form is based on the User model
class UserRegistrationForm(forms.ModelForm):
    # Add a field to ask if the user is registering as a Company
    is_company = forms.BooleanField(required=False, label='Register as a Company')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_company', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # Set the is_company flag based on the checkbox
        user.is_company = self.cleaned_data["is_company"]
        if commit:
            user.save()
        return user