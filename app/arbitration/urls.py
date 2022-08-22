from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .api import *
from .views import *
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path('api/getexchanges/', get_exchanges),
    path('api/delete/', dropping_exchanges),
    path('api/postexchanges/', post_exchanges),
    path('api/registrationuser/', registration_user),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('test/', testEndPoint, name='test'),
    path('', get_routes)
] + router.urls
