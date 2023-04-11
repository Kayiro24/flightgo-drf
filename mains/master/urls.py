from django.urls import re_path, include
from .views import AircraftSetViewList, AirportSetViewList
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('aircraft', AircraftSetViewList, 'aircraft')
router.register('airport', AirportSetViewList, 'airport')


urlpatterns = [
    re_path('', include(router.urls)),
]