from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_request(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/index")
        else:
            return render(request, "account/login.html", {
                "error": "Try Again. Username or password wrong !",
            })

    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re-password"]
        lastname = request.POST["lastname"]
        firstname = request.POST["firstname"]

        user_info = {
            "username": username,
            "email": email,
            "lastname": lastname,
            "firstname": firstname,
        }

        if password.__eq__(re_password):
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error": "Username is not valid !",
                    "user": user_info,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {
                        "error": "Email is not valid !",
                        "user": user_info,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname,
                                                    last_name=lastname, password=password)
                    user.save()
                    return redirect("login")

        else:
            return render(request, "account/register.html", {
                "error": "Password is not match !",
                "user": user_info,
            })

    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("/index")
