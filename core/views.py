from allauth.account import app_settings
from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


@login_required
def secret(request):
    return render(request, 'secret.html')


class CustomSignupView(SignupView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = 'Welcome to the custom signup page!'
        return context
    
    def form_valid(self, form):
        # Add custom logic here before saving the user
        response = super().form_valid(form)

        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
            messages.info(self.request, 'Please verify your email address to complete the registration.')
        else:
            messages.success(self.request, 'You have signed up successfully!')
        return response
