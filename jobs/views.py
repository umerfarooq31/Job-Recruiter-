# --- jobs/views.py ---

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Job
from .forms import JobCreationForm
from accounts.models import Company


# Helper function to check if a user is a company
def is_company(user):
    return user.is_authenticated and user.is_company


# The main job list and search page (Homepage)
def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')

    search_query = request.GET.get('q')
    location_query = request.GET.get('location')

    if search_query:
        # Search in title, description, and company name
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(company__name__icontains=search_query)
        )

    if location_query:
        # Filter by job location
        jobs = jobs.filter(location__icontains=location_query)

    context = {
        'jobs': jobs,
        'search_query': search_query or '',
        'location_query': location_query or ''
    }
    return render(request, 'jobs/job_list.html', context)


# Page to view a single job
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


# Page for a company to create a new job
@login_required
@user_passes_test(is_company)  # Only companies can access this
def job_create(request):
    # This line now works because the Company profile is automatically created via the Signal
    company_profile = get_object_or_404(Company, user=request.user)

    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company_profile  # Link the job to the posting company
            job.save()
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobCreationForm()

    return render(request, 'jobs/job_create.html', {'form': form})