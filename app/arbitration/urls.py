from rest_framework import routers
from .api import *
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path('api/getexchanges/', get_exchanges),
    path('api/postexchanges/', post_exchanges),
    path('api/sendveremail/', send_verification_message),
] + router.urls
