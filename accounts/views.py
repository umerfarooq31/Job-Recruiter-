from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


# This view handles the user registration process
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after successful registration
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})