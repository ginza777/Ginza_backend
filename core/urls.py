from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .schema import swagger_urlpatterns
from apps.GinzaApi.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView, name="home"),
    path("", include("apps.GinzaApi.urls")),
    path("", include("apps.GinzaAuthUser.urls")),
    path("", include("apps.DjangoFilterBackend.urls")),

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
