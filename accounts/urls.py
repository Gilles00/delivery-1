from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    CustomPasswordChangeView, CustomLoginView, profile, registration)

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('register/', registration, name='register'),
    path('profile/', profile, name='profile'),
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
]
