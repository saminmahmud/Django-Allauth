from django.contrib import admin
from django.urls import include, path
from core.views import CustomSignupView, index, secret

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),  # must be before the allauth urls inclusion  
    path('accounts/', include('allauth.urls')),

    path('', index, name='index'),
    path('secret/', secret, name='secret'),
]
