from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


# Violate architecture patterns DDD
# needs to create a intermediate layer
# and refactor to never calls models in view
from users.models import User
# Create your views here.

def create_user(request):
    res = User.userManager.register(**request.POST)
    if res[0]:
        request.session['user_id'] = res[1]
        return redirect(reverse('dashboard:index'))
    else:
        for message in res[1]:
            messages.warning(request, message)
        return redirect(reverse('login:index'))


