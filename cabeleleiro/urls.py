
from django.contrib import admin
from django.urls import path, include
from cabeleleiroapp.views import index
from cabeleleiroapp.views import geracode
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', include('usuarios.urls')),
    path('geracode/', geracode, name='geracode'),
]
