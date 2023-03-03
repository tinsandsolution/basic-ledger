from django.urls import path

urlpatterns = [
    # path('accounts/', admin.site.urls),


    # path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    # path('user/login/', ObtainTokenPair.as_view(), name='token_create'),
    # path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('user/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # path('user/hello/', Hello.as_view(), name='hello')
]

'''
get all accounts by the current user
accounts/, get

create account for the current user
accounts/, post

create a transaction for the current user
accounts/<int:account_id>, post

get balance of an account
accounts/<int:account_id>, get

'''
