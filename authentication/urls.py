from django.urls import path

import authentication.views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',
        redirect_authenticated_user=True,
    ), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
        redirect_authenticated_user=True,
    ), name='password_change_done'),
    # path("logout/", authentication.views.logout_user, name="logout"),
]
