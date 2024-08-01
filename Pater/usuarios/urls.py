from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

urlpatterns = [
    path('login/', views.login_request , name='Login'),
    path('register/', views.registro, name='Register'),
    path('logout/', LogoutView.as_view(template_name='cursos/inicio.html'), name='Logout'),
]