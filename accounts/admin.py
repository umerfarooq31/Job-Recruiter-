
from django.contrib import admin
from .models import User, Company

# Register the custom User model
admin.site.register(User)

# Register the Company profile model
admin.site.register(Company) 

