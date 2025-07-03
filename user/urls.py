from django.urls import path
from .views import register, verify_otp
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('register-page/', TemplateView.as_view(template_name='user/register.html'), name='register-page'),
    path('otp-page/<str:email>/<str:phone>/<str:password>/<int:otp>/', TemplateView.as_view(template_name='user/otp.html'), name='otp-page'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('successpage/', TemplateView.as_view(template_name='user/successpage.html'), name='successpage'),
]