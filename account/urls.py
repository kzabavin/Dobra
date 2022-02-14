from django.urls import path
from django.contrib.auth import views

from .views import dashboard

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    #path('logout-then-login/', 'views.logout_then_login', name='logout_then_login'),
    #path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # Затем вам нужно добавить шаблон registration/password_reset_form.html
    # Таким же образом, вам нужно добавить шаблоны password_reset_confirm.html, password_reset_done.html, password_reset_email.html и password_reset_complete.html.
    #path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('', dashboard, name='dashboard'),

]