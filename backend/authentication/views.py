from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from typing import Dict

from users.models import User


def reply400(message: str) -> Dict:
    return Response({'error': f'{message}'}, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_admin(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return  reply400('Please provide both username and password')

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return  reply400('Please provide both username and password')

    # needs to create intermediate functions
    # don't import Models in Views.py
    # violate architecture
    import pdb; pdb.set_trace()
    user = User.objects.get(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user)
    return Response({'token': token.key}, status=HTTP_200_OK)
