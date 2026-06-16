from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
