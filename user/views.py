from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
from .tasks import send_welcome_email
from .models import CustomUser
import random

def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            # Save the user data
            user = serializer.validated_data
            # Generate and send OTP
            otp = str(random.randint(100000, 999999))
            send_welcome_email.delay(user['email'], otp)
            # Redirect to OTP page with registration data
            return redirect('user:otp-page', email=user['email'], phone=user['phone'], password=user['password'], otp=otp)
        return render(request, 'user/register.html', {'errors': serializer.errors})
    return render(request, 'user/register.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        gen_otp = request.POST.get('gen_otp')
        otp = request.POST.get('otp')

        print("Email:", email)
        print("Phone:", phone)
        print("Password:", password)
        print("Generated OTP:", gen_otp)
        print("Entered OTP:", otp)

        if not all([email, phone, password, gen_otp, otp]):
            return render(request, 'user/otp.html', {
                'error': 'Invalid form submission. Please try again.',
                'email': email,
                'phone': phone,
                'password': password,
                'gen_otp': gen_otp
            })

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'user/otp.html', {
                'error': 'This email is already registered. Please use a different email.',
                'email': email,
                'phone': phone,
                'password': password,
                'gen_otp': gen_otp
            })
        
        # Verify OTP logic here
        if otp == gen_otp:
            try:
                # OTP is valid and email is unique, proceed with registration
                user = CustomUser.objects.create_user(email=email, phone=phone)
                user.set_password(password)
                user.save()
                return redirect('user:successpage')
            except Exception as e:
                return render(request, 'user/otp.html', {
                    'error': f'Error creating user: {str(e)}',
                    'email': email,
                    'phone': phone,
                    'password': password,
                    'gen_otp': gen_otp
                })
        else:
            return render(request, 'user/otp.html', {
                'error': 'Invalid OTP. Please try again.',
                'email': email,
                'phone': phone,
                'password': password,
                'gen_otp': gen_otp
            })
    return redirect('user:register')