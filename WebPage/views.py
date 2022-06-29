from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    return render(request, 'Anasayfa.html')


def urunler(request):
    return render(request, 'Urunler.html')


def hakkimizda(request):
    return render(request, 'Hakkimizda.html')


def iletisim(request):
    return render(request, 'Iletisim.html')


def uyeol(request):
    if request.method == "POST":
        form = UserSigninForm(request.POST)
        if form.is_valid():
            Customer = form.save(commit=False)
            login(request, Customer)
            Customer.save()
            return redirect("http://127.0.0.1:8000/Anasayfa")
    else:
        form = UserSigninForm()
    return render(request, 'Uyeol.html', {'form': form})


def giris(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/Anasayfa")
            else:
                messages.error(request, 'Kullanıcı adı ya da şifre hatalı')
                return redirect("http://127.0.0.1:8000/Giris")
    else:
        form = UserLoginForm()
    return render(request, "Giris.html", {'form': form})


@login_required(login_url="http://127.0.0.1:8000/Giris")
def cikis(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/Anasayfa")
