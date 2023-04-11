from django.urls import re_path, include
from rest_framework import routers
from .views import RegisterUser, RegisterPassenger


router = routers.SimpleRouter()
router.register('user', RegisterUser, "registeruser")
router.register('passenger', RegisterPassenger, "registerpassenger")


urlpatterns = [
    re_path("", include(router.urls))
]