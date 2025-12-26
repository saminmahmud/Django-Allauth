from django.contrib import admin
from django.urls import include, path

from core.views import index, secret

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('', index, name='index'),
    path('secret/', secret, name='secret'),
]
