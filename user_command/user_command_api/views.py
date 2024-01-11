from rest_framework import viewsets

from .models import User, Command
from .serializers import UserSerializer, CommandSerializer

"""
I use Viewset like efficient way to handle common CRUD. It provide a high level of abstraction and consistency.
If it will be necessary we can use APIView in this application also. APIView is more flexibility and control.
"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
