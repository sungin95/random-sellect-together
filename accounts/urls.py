from django.urls import path, include

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("delete/", views.delete, name="user_delete"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
]
