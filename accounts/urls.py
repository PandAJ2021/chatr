from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.UserRegisterView.as_view(), name='register_user'),
    path('login/', views.UserLoginView.as_view(), name='login_user'),
    path('logout/', views.UserLogOutView.as_view(), name='logout_user'),
]