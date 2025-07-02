from django.urls import path
from .views import RegisterView, SendEmail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('send-email/', SendEmail.as_view(), name='send-email'),
]