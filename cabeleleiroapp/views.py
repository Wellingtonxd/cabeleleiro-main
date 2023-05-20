from django.contrib.auth.decorators import login_required
from usuarios.models import Ruan
from django.shortcuts import render
from qrcode import*
data = None


def geracode(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img.save('cabeleleiroapp/static/img/qrcode1.png')
    else:
        pass
    return render(request, 'cabeleleiro/geracode.html',{"data": data})


@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    dados = Ruan.objects.filter(username=str(request.user.username))
    return render(request,'cabeleleiro/index.html',{"perfil": dados})


