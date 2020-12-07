from django.urls import path
from loans.views import *

urlpatterns = [

    # function based views
    path('client/(<client_id>)/loan/apply/', name='clientloanapplication'),
    path('client/(<client_id>)/loans/list/', name="clientloanaccountslist"),
    path('client/loan/(<pk>)/view/', name='clientloanaccount'),
    path('client/(<client_id>)/loan/(<loanaccount_id>)/deposits/list/', name='listofclientloandeposits'),
    path('client/(<client_id>)/loan/(<loanaccount_id>)/ledger/', name="clientloanledgeraccount"),
    path('client/(<client_id>)/loan/(<loanaccount_id>)/ledger/download/csv/', client_ledger_csv_download,
         name="clientledgercsvdownload"),
    path('client/(<client_id>)/loan/(<loanaccount_id>)/ledger/download/excel/', client_ledger_excel_download,
        name="clientledgerexceldownload"),
    path('client/(<client_id>)/loan/(<loanaccount_id>)/ledger/download/pdf/', client_ledger_pdf_download,
        name="clientledgerpdfdownload"),
    path('group/(<group_id>)/loan/apply/',
         group_loan_application, name='grouploanapplication'),
    path('group/(<group_id>)/loans/list/',
         group_loan_list, name="grouploanaccountslist"),
    path('group/loan/(<pk>)/view/',
         group_loan_account, name='grouploanaccount'),
    path('group/(<group_id>)/loan/(<loanaccount_id>)/deposits/list/',
         group_loan_deposits_list, name='viewgrouploandeposits'),
    path('loan/(<pk>)/change-status/',
         change_loan_account_status, name='change_loan_account_status'),
    path('loan/(<loanaccount_id>)/issue/', issue_loan, name='issueloan'),
]
