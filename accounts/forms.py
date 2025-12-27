from django import forms
from .models import UserProfile


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone = forms.CharField(max_length=15, label='Phone Number', required=False)

    def signup(self, request, user):
        # Save the additional fields to the user model
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Create or update the UserProfile
        profile = UserProfile(user=user)
        profile.phone = self.cleaned_data.get('phone', '')
        profile.save()