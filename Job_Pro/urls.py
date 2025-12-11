# --- job_board_project/urls.py ---

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs for the jobs app (like the homepage and listings)
    path('', include('jobs.urls')), 
    # URLs for the accounts app (like login and register)
    path('accounts/', include('accounts.urls')), 
]