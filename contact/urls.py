from django.urls import path, re_path

from contact import views


urlpatterns = [
    path('contact/', views.message, name='contact'),
    path("thanks/", views.thanks, name="thanks"),
]
 