from django.urls import path, re_path

from accounts import views


urlpatterns = [
    # path("profile/<str:pk>/", views.profile, name="profile"),

    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    path("profile/<str:pk>/", views.profile, name="profile"),
    path("profile/", views.profile, name="profile"),
    path("email/confirmation/", views.activation_message,
         name="activation_message"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate_email, name='activate'),
    path("sampletemp/", views.sampletemp, name="sampletemp"),
    path("personal/<str:pk>/details/",
         views.PersonalDetailsView.as_view(), name="personal_details"),
    path("origin/<str:pk>/details/",
         views.OriginDetailsView.as_view(), name="origin_details"),
    path("nysc/<str:pk>/details/",
         views.NYSCDetailsView.as_view(), name="nysc_details"),
    path("professional/<str:pk>/details/",
         views.ProfessionalDetailsView.as_view(), name="profesional_details"),
    path("picture/<str:pk>/details/",
         views.PhotosView.as_view(), name="profile_picture"),
]
