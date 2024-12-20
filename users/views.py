from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from users.serializers import SignupSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully", "username": user.username},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Validate input
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # verifying credentials
        user = authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed("Incorrect username or password")

        # generating JWT
        access_token = AccessToken.for_user(user)

        # building the response
        response = Response(
            {
                "message": "Login successful",
                "access_token": str(access_token),
            }
        )

        response.set_cookie(
            key="auth_token",
            value=str(access_token),
            httponly=True,
            secure=settings.SECURE_COOKIES,
            samesite="Lax",
        )

        return response
