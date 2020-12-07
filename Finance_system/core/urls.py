from django.urls import path
from core.views import receipts_deposit, client_loan_accounts_view, get_loan_demands_view, payslip_create_view, get_group_loan_accounts, \
    get_member_loan_accounts, get_fixed_deposit_accounts_view, get_recurring_deposit_accounts_view, client_deposit_accounts_view, \
    get_fixed_deposit_paid_accounts_view, get_recurring_deposit_paid_accounts_view

urlpatterns = [
    path('receiptsdeposit/', receipts_deposit, name="receiptsdeposit"),
    path('getmemberloanaccounts/', client_loan_accounts_view,
         name="getmemberloanaccounts"),
    path('getloandemands/', get_loan_demands_view, name="getloandemands"),
    path('payslip/', payslip_create_view, name="payslip"),
    path('loanaccounts/group', get_group_loan_accounts,
         name="get_group_loan_accounts"),
    path('loanaccounts/member', get_member_loan_accounts,
         name="get_member_loan_accounts"),
    path('getmemberfixeddepositaccounts/',
         get_fixed_deposit_accounts_view, name="getmemberfixeddepositaccounts"),
    path('getmemberrecurringdepositaccounts/',
         get_recurring_deposit_accounts_view, name="getmemberrecurringdepositaccounts"),
    path('getmemberdepositaccounts/', client_deposit_accounts_view,
         name="getmemberdepositaccounts"),
    path('getmemberfixeddepositpaidaccounts/',
         get_fixed_deposit_paid_accounts_view, name="getmemberfixeddepositpaidaccounts"),
    path('getmemberrecurringdepositpaidaccounts/',
         get_recurring_deposit_paid_accounts_view, name="getmemberrecurringdepositpaidaccounts"),
]
