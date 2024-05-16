"""
URL configuration for jnexus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.routers import DefaultRouter
# from Product.views import ProductViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="TBC Swagger",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
# router.register(r'api/product', ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api/account/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/account/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('api/account/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
    path('api/account/', include("acl.urls")),
    path('', include(router.urls)),
]
