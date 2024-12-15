
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from accounts.views import (
    user_registration_viewset,
    user_login_viewset,
    user_logout_viewset,
    user_viewset,
)

urlpatterns = [
    path(
        "renew-token/",
        TokenRefreshView.as_view(),
        name="renew-token",
    ),
    path(
        "verify-token/",
        TokenVerifyView.as_view(),
        name="verify-token",
    ),
    path("register/",user_registration_viewset.UserRegistrationViewset.as_view(),
        name="register",
    ),
    path("login/",user_login_viewset.LoginView.as_view(),
        name="login",
    ),
    path("logout/",user_logout_viewset.LogoutView.as_view(),
        name="logout",
    ),
    path('users/', user_viewset.UserListCreateAPIView.as_view(), 
         name='user-list-create',
    ),
    path('users/<int:pk>/', user_viewset.UserDetailAPIView.as_view(), 
         name='user-detail',
    ),
]