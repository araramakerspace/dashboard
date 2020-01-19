from django.shortcuts import render


# Violate architecture patterns DDD
# needs to create a intermediate layer
# and refactor to never calls models in view
from users.models import User
# Create your views here.

def create_user(request):
    pass

