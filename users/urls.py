from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserUpdateApiView, UserRetrieveApiView, UserDestroyApiView
app_name = UsersConfig.name

urlpatterns = [
    path('/user/create/', UserCreateApiView.as_view(), name='create'),
    path('/user/update/<int:pk>/', UserUpdateApiView.as_view(), name='update'),
    path('/user/retrieve/<int:pk>/', UserRetrieveApiView.as_view(), name='retrieve'),
    path('/user/destroy/<int:pk>/', UserDestroyApiView.as_view(), name='destroy'),

    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token-Obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-Refresh'),
]
