
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from accounts import views_api as accounts_views_api

router = DefaultRouter()
router.register(r"account", accounts_views_api.AccountViewSet, basename='account')


urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("securelogin/", admin.site.urls),
    path("", views.home, name="home"),
    path("store/", include("store.urls")),
    path("cart/", include("carts.urls")),
    path("accounts/", include("accounts.urls")),

    # ORDERS
    path("orders/", include("orders.urls")),

    # DRF
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
