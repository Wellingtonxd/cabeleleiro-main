from django.contrib import admin
from django.urls import path
from cabeleleiroapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', views.geracode, name='geracode'),
    path('geracode', views.geracode),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
