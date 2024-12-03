from django.urls import path
from property_app.views import Propertyview,Tenantview,Leaseview,Unitview


urlpatterns=[

  path('property',Propertyview.as_view(),name='property'),
  path('tenant',Tenantview.as_view(),name='tenant'),
  path('lease',Leaseview.as_view(),name='lease'),
  path('unit',Unitview.as_view(),name='unit'),
]