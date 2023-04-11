from django.urls import re_path, include
from .views import SearchFlightViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', SearchFlightViewSet, "searchflight")


urlpatterns = [
    re_path('', include(router.urls)),    
]