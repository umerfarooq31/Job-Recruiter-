from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# We extend the base Django User model to add an 'is_company' flag
class User(AbstractUser):
    # This flag helps us separate job seekers from company users
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# This model holds extra information for company users
class Company(models.Model):
    # Link to the User who represents this company
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, default="New Company")  # Added default
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name



# This function runs every time a User object is saved.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Check if this user is flagged as a company
    if instance.is_company:

        # If the user was just created (first time saved):
        if created:
            # Create a new Company profile linked to this user, giving it a default name
            Company.objects.create(user=instance, name=f"{instance.username}'s Company")

        # This handles cases where the user might already exist but their profile
        # needs to be saved/checked (e.g., if they were created before the signal was active)
        try:
            instance.company.save()
        except Company.DoesNotExist:
            Company.objects.create(user=instance, name=f"{instance.username}'s Company")