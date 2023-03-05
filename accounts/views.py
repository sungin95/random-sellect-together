from django.shortcuts import render
from django.contrib.auth import get_user_model


def index(request):
    user = get_user_model().objects.get(pk=request.user.pk)  # 로그인 한 유저
    context = {
        "user": user,
    }
    return render(request, "accounts/index.html", context)
