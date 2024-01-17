from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from .models import *
# class DisplayUsers(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         return Response(serializers.serialize('json', users), status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user is None:
            return Response({'message': 'Invalid email id'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if check_password(password, user.password):
            login(request, user)
            request.session['current_user'] = user.email
            return Response({'message': 'User accepted'}, status=status.HTTP_202_ACCEPTED)
        return Response({'error':'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateUserView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(email, password)
            if user is not None:
                login(request, user)
                request.session['current_user'] = user.email
                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:  # Handle potential errors
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IsLoggedIn(APIView):
    def get(self, request, format=None):
        if not request.session.session_key:
            request.session.create()
        if request.session.get('current_user', None) is not None:
            user = User.objects.get(email=request.session['current_user'])
            return Response({'result': user.is_authenticated}, status=status.HTTP_200_OK)
        return Response({'result': False}, status=status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request, format=None):
        if request.session.get('current_user', None) is not None:
            del request.session['current_user']
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)