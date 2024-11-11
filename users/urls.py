from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import (
    login_view,
    logout_view,
    register_view,
    users_list_view,
    profile_view,
)


urlpatterns = [
    path(
        "login/",
        login_view,
        name="login",
    ),
    path(
        "logout/",
        logout_view,
        name="logout",
    ),
    path("register/", register_view, name="register"),
    path("list/", users_list_view, name="users_list"),
    path("profile/", profile_view, name="profile"),
]
