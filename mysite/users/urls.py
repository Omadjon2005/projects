from django.urls import path
from users.views import signUp,profile
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('signUp/',signUp,name='signUp-page'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login-page'),
    path('logout/',LogoutView.as_view(template_name='users/Logout.html'),name='logout-page'),
    path('profile/',profile,name='profile-page'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
     PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
























