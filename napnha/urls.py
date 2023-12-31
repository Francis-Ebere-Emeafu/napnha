from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    # path("register", TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    # path("login", TemplateView.as_view(template_name="accounts/login.html"), name="login"),
    path("about", TemplateView.as_view(template_name="about.html"), name="about"),
    path("mission", TemplateView.as_view(
        template_name="mission.html"), name="mission"),
    path("vision", TemplateView.as_view(
        template_name="vision.html"), name="vision"),
    # path("contact", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path("accounts/", include("accounts.urls")),
    path("", include("contact.urls")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


"""napnha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
