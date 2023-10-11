from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from wallets.views import WalletViewSet

router = DefaultRouter()
router.register(r"wallets", WalletViewSet, "wallet")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    re_path(r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve,
            {"document_root": settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)