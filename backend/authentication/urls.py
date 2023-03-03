from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, CustomUserCreate, Hello

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/login/', ObtainTokenPair.as_view(), name='token_create'),
    path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('user/hello/', Hello.as_view(), name='hello')
]
