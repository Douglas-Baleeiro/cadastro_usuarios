from django.urls import path
from app_cad_usuarios import views  

#criar rota, view e nome de referência
urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios,name='listagem_usuarios')
]
