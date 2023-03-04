from django.urls import path
from .views import AccountCreate,AccountManager

urlpatterns = [
    path('', AccountCreate.as_view(), name="all_accounts"),
    path('<int:account_id>/', AccountManager.as_view(), name="manage_account")
]
