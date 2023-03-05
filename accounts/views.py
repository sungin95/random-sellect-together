from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def index(request):
    user = get_user_model().objects.get(pk=request.user.pk)  # 로그인 한 유저
    context = {
        "user": user,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 회원가입과 동시에 로그인을 시키기 위해
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:  # 로그인이 된 상태에서는 로그인 화면에 들어갈 수 없다.
        return redirect("accounts:index")
    if request.method == "POST":
        form = AuthenticationForm(
            request, data=request.POST
        )  # request가 없어도 잘 돌아가는거 같음 하지만 대부분이 request를 필수적으로 받아 가지고 편의상 넣겠음
        if form.is_valid():
            auth_login(request, form.get_user())  # login을 가져와야 한다.
            return redirect(
                request.GET.get("next") or "accounts:index"
            )  # login_required를 사용하기 위해
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context=context)


from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)
