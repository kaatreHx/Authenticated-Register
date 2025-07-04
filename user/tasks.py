from celery import shared_task
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMessage

@shared_task
def send_welcome_email(user_email, otp):
    email = EmailMessage(
        subject='Welcome to our platform!',
        body=f'Thank you for registering with us. Your OTP is {otp}',
        from_email='bobmagarketa@gmail.com',
        to=[user_email],
    )
    email.send()