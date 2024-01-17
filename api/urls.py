from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('sign-up', CreateUserView.as_view(), name='signup'),
    path('is-logged-in', IsLoggedIn.as_view(), name='isLoggedIn'),
    path('logout', Logout.as_view(), name='logout'),
]