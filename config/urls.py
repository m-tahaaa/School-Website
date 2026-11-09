from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("school.urls")),
    path("assets/<path:path>", serve, {"document_root": settings.BASE_DIR / "static" / "assets"}),
    path("favicon.ico", RedirectView.as_view(url="/assets/favicon.svg")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
