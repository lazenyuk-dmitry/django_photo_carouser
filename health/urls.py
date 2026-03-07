from django.urls import path
from health.views import health_check_custom

urlpatterns = [
    path('healthz/', health_check_custom)
]
