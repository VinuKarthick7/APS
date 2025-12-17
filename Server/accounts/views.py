from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Headers:", request.headers)
        uid = request.data.get("uid")
        password = request.data.get("password")

        user = authenticate(request, uid=uid, password=password)


        if not user:
            return Response({"error": "Invalid credentials"}, status=401)

        refresh = RefreshToken.for_user(user)

        return Response({
            "token": str(refresh.access_token),
            "user": UserSerializer(user).data
        })

