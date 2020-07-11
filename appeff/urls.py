from django.urls import path, include
from .views import login, home
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home, name="index"),
    path('login', login, name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
]