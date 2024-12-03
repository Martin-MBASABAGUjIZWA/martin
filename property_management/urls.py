
from django.contrib import admin
from django.urls import path,include
from property_app.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('p1/v1/',include('property_app.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/p1/p1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', home, name='home'),
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('property_app/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('property_app/Unit', unit_list, name='unit_list'),
    path('property_app/Property', property_list, name='property_list'),
    path('property_app/Property/<int:pk>/', property_list, name='property_list'),
    path('property_app/Tenant', tenant_list, name='tenant_list'),
    path('property_app/Lease',lease_list, name='lease_list'),
    # path('unit/',Units_test.as_view(),name='units_test'),
    path('admin/', admin.site.urls),
]

