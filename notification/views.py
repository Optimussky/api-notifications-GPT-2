from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Notification
from .serializers import NotificationSerializer, LoginSerializer
from django.utils import timezone
# Create your views here.

# Vista para login y obtener el token JWT
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')

            if username is None or password is None:
                return Response({'error': 'Se requieren nombre de usuario y contraseña'}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'auth': True, 'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        

        return Response({'error': 'Contraseña incorrecta' if User.objects.filter(username=username).exists() else 'Usuario no encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

# Vista para enviar notificación por correo
class SendNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)

        if serializer.is_valid():
            # Código para el envío del correo electrónico
            # send_mail(notification.title, notification.body, 'from@example.com',[notification.email])
            print(serializer)
            return Response({'date': timezone.now(), 'message': 'Correo Electrónico enviado exitosamente.'}, status=status.HTTP_200_OK),serializer

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



