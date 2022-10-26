from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from company_users.serializers import (
    RegisterUserSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def CustomUserCreate(request):
    permission_classes = [AllowAny]
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        newuser = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def BlacklistTokenView():
    permission_classes = [AllowAny]
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
