from django.contrib.auth import get_user_model, login
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserLoginSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserCreateSerializer


class LoginUserView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def get_response(self):
        data = {
            'id': self.user.id,
            'username': self.user.username,
            'status_code': status.HTTP_200_OK
        }
        return Response({"data": data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)
        self.is_valid = self.serializer.is_valid()
        if not self.is_valid:
            return Response({"data": self.serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        self.user = self.serializer.validated_data['user']
        if self.user:
            login(request=request, user=self.user)
        return self.get_response()
