from django.urls import path
from .views import AccountCreate,AccountManager, AccountTransactions, AllTransactions

urlpatterns = [
    path('', AccountCreate.as_view(), name="all_accounts"),
    path('<int:account_id>/', AccountManager.as_view(), name="manage_account"),
    path('<int:account_id>/transactions/', AccountTransactions.as_view(), name="account_transactions"),
    path('transactions/all/', AllTransactions.as_view(), name="all_transactions")
]
