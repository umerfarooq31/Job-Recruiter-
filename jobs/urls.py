# # --- jobs/urls.py ---
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.job_list, name='job_list'),
#     path('job/<int:pk>/', views.job_detail, name='job_detail'),
#     path('job/new/', views.job_create, name='job_create'),
# ]
# --- jobs/urls.py ---

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/new/', views.job_create, name='job_create'), # <--- THIS IS THE KEY LINE
]