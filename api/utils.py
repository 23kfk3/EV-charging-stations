from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from .models import User
# from django.contrib.auth.decorators import login_required

def create_user(email, password):
    user = User.objects.create_user(email, password)
    return user

def login_user(email, password):
    user = User.objects.get(email=email)
    if check_password(password, user.password):
        return user
    else:
        return None