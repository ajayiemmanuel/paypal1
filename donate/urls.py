from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path ('verify', views.verify, name = "verify"),
    path ('blog/', views.blog, name = "blog"),
]