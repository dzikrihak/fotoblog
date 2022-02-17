from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

import authentication.views
import blog.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('authentication.urls')),
    # mempersingkat kode tanpa harus membuat LoginPageView di views
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',
    ), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password_change_done'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    # path("", authentication.views.login_page, name="login_fbv"),
    # path("", authentication.views.LoginPageView.as_view(), name='login'),
    # path("logout/", authentication.views.logout_user, name='logout'),
    path("home/", blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )