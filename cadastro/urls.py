from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lista', views.lista_all, name='lista'),
]