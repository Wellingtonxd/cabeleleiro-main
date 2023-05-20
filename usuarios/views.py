from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from.models import Ruan
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('Username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # verifica se o cpf ja esta em uso
        user = User.objects.filter(username=username).first()


        if user:
            # caso ele exista esse codigo o informará
            return HttpResponse('ja existe um usuario com esse nome')
        # caso nao ele ira criar um novo, com o cpf sendo o username e a senha a data de nascimento
        user = User.objects.create_user(username=username, password=senha)
        dado = Ruan.objects.create(username=username, email=email, senha=senha)
        return redirect('http://127.0.0.1:8000/index/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:

        username = request.POST.get('Username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)

            return redirect('http://127.0.0.1:8000/index/')
        else:
            return HttpResponse('usuario não encontrado')
