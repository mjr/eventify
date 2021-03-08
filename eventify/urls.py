from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


admin.site.enable_nav_sidebar = False

urlpatterns = [
    path("api/v1/", include("eventify.api.urls")),
    path("authentication/", include("rest_framework.urls")),
    path("restricted/", admin.site.urls),
    path("admin/", RedirectView.as_view(url="https://www.djangoproject.com")),
]
