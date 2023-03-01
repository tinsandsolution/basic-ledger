from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, CustomUserCreate

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/login/', ObtainTokenPair.as_view(), name='token_create'),
    path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
