from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterUserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = []

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        user = User.objects.get(username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user) 
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def list(self, request):
        return self.retrieve(request, pk=request.user.pk)