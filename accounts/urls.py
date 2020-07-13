from django.urls import path, re_path

from accounts import views


urlpatterns = [
    # path("profile/<str:pk>/", views.profile, name="profile"),
    # path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),

    path("profile/", views.profile, name="profile"),
    path("email/confirmation/", views.activation_message, name="activation_message"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_email, name='activate'),
]
