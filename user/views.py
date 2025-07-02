from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .tasks import send_welcome_email

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendEmail(APIView):
    def post(self, request):
        send_welcome_email.delay(request.data['email'])
        return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)